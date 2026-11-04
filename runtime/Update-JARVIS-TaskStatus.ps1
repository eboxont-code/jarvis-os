[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidateSet('Start', 'Finish')][string]$Action,
    [Parameter(Mandatory)][string]$TaskText,
    [ValidateSet('PARTIAL', 'BLOCKED', 'VERIFIED')][string]$Status,
    [string]$Evidence,
    [string]$Done,
    [string]$Remaining,
    [string]$NextAction,
    [string]$StatusRowLabel
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-BoundedGit {
    param([string]$Git, [string[]]$Arguments, [int]$TimeoutSeconds = 45)

    $quoted = foreach ($arg in $Arguments) {
        '"' + ([string]$arg).Replace('"', '\"') + '"'
    }

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $Git
    $psi.Arguments = ($quoted -join ' ')
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.StandardOutputEncoding = [Text.Encoding]::UTF8
    $psi.StandardErrorEncoding = [Text.Encoding]::UTF8

    $p = New-Object System.Diagnostics.Process
    $p.StartInfo = $psi
    try {
        [void]$p.Start()
        $outTask = $p.StandardOutput.ReadToEndAsync()
        $errTask = $p.StandardError.ReadToEndAsync()
        if (-not $p.WaitForExit($TimeoutSeconds * 1000)) {
            try { $p.Kill() } catch {}
            throw "Git command timed out after $TimeoutSeconds seconds: $($Arguments -join ' ')"
        }
        $p.WaitForExit()
        $out = $outTask.GetAwaiter().GetResult()
        $err = $errTask.GetAwaiter().GetResult()
        if ($p.ExitCode -ne 0) {
            throw ("Git failed (exit {0}): git {1}{2}{3}" -f $p.ExitCode, ($Arguments -join ' '), [Environment]::NewLine, (($out, $err) -join [Environment]::NewLine))
        }
        return $out
    }
    finally {
        $p.Dispose()
    }
}

function Clean-Cell([string]$Value) {
    return (($Value -replace '[\r\n]+', ' ') -replace '\|', '\|').Trim()
}

try {
    if ([string]::IsNullOrWhiteSpace($TaskText)) { throw 'TaskText cannot be empty.' }

    if ($Action -eq 'Finish') {
        if ($Status -eq 'VERIFIED' -and [string]::IsNullOrWhiteSpace($Evidence)) {
            throw 'VERIFIED requires concrete test evidence.'
        }
        if ($Status -eq 'PARTIAL' -and ([string]::IsNullOrWhiteSpace($Done) -or [string]::IsNullOrWhiteSpace($Remaining))) {
            throw 'PARTIAL requires both Done and Remaining.'
        }
        if ($Status -eq 'BLOCKED' -and ([string]::IsNullOrWhiteSpace($Evidence) -or [string]::IsNullOrWhiteSpace($NextAction))) {
            throw 'BLOCKED requires the blocker in Evidence and a concrete NextAction.'
        }
    }

    $repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
    $masterPath = Join-Path $repoRoot 'MASTER_TODO.md'
    if (-not (Test-Path -LiteralPath $masterPath -PathType Leaf)) { throw 'MASTER_TODO.md not found.' }

    $git = (Get-Command git -ErrorAction Stop).Source
    $oldPrompt = $env:GIT_TERMINAL_PROMPT
    $oldGcm = $env:GCM_INTERACTIVE
    $env:GIT_TERMINAL_PROMPT = '0'
    $env:GCM_INTERACTIVE = 'never'

    try {
        $branch = (Invoke-BoundedGit $git @('-C', $repoRoot, 'branch', '--show-current')).Trim()
        if ($branch -ne 'main') { throw "Expected branch main; current branch is '$branch'." }

        $origin = (Invoke-BoundedGit $git @('-C', $repoRoot, 'remote', 'get-url', 'origin')).Trim()
        if ($origin -notmatch '^(https://github\.com/eboxont-code/jarvis-os(?:\.git)?/?|git@github\.com:eboxont-code/jarvis-os(?:\.git)?)$') {
            throw "Unexpected origin remote: $origin"
        }

        $dirty = Invoke-BoundedGit $git @('-C', $repoRoot, 'status', '--porcelain', '--', 'MASTER_TODO.md')
        if (-not [string]::IsNullOrWhiteSpace($dirty)) {
            throw 'MASTER_TODO.md has local or staged changes. They were not overwritten or committed.'
        }

        Write-Host 'Refreshing the private master checklist...' -ForegroundColor Cyan
        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'fetch', '--no-tags', 'origin', 'main'))
        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'merge', '--ff-only', 'FETCH_HEAD'))
        $localBase = (Invoke-BoundedGit $git @('-C', $repoRoot, 'rev-parse', 'HEAD')).Trim()
        $remoteBase = (Invoke-BoundedGit $git @('-C', $repoRoot, 'rev-parse', 'FETCH_HEAD')).Trim()
        if ($localBase -ne $remoteBase) {
            throw 'Local main is ahead of or diverged from GitHub. The controller will not push pre-existing local commits.'
        }

        $content = [IO.File]::ReadAllText($masterPath, [Text.Encoding]::UTF8)
        $newline = [Environment]::NewLine
        $lines = $content -split '\r?\n'
        $matches = @()
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match '^\s*-\s\[[ x]\]' -and $lines[$i].IndexOf($TaskText, [StringComparison]::OrdinalIgnoreCase) -ge 0) {
                $matches += $i
            }
        }

        if ($matches.Count -ne 1) {
            throw "Expected one task checkbox containing '$TaskText'; found $($matches.Count). No file was changed. Use a more specific TaskText."
        }

        $taskIndex = [int]$matches[0]
        $taskLine = $lines[$taskIndex]

        if ($Action -eq 'Start') {
            if ($taskLine -match '\*\*WORKING\*\*') {
                Write-Host 'This task is already marked WORKING.' -ForegroundColor Yellow
                exit 0
            }
            if ($taskLine -match '^\s*-\s\[x\]') {
                throw 'This task is already checked. Do not restart a VERIFIED task without first reviewing its evidence.'
            }

            $active = @($lines | Where-Object { $_ -match '^\s*-\s\[\s\]\s+\*\*WORKING\*\*' })
            if ($active.Count -gt 0) {
                throw "Another task is already WORKING: $($active -join '; '). Finish or mark it PARTIAL/BLOCKED first."
            }

            $description = $taskLine -replace '^\s*-\s\[\s\]\s*', ''
            $lines[$taskIndex] = '- [ ] **WORKING** — ' + $description
            $logStatus = 'WORKING'
            $logEvidence = 'Task selected by the local project controller.'
            $logNext = 'Execute the task and record actual tests.'
        }
        else {
            if ($taskLine -notmatch '\*\*WORKING\*\*') {
                throw 'Finish requires the task to be marked WORKING first.'
            }

            $description = $taskLine -replace '^\s*-\s\[\s\]\s+\*\*WORKING\*\*\s+[—-]\s*', ''
            switch ($Status) {
                'VERIFIED' {
                    $lines[$taskIndex] = '- [x] **VERIFIED** — ' + $description + ' — evidence: ' + (Clean-Cell $Evidence)
                    $logEvidence = Clean-Cell $Evidence
                    $logNext = 'Select the next eligible task.'
                }
                'PARTIAL' {
                    $lines[$taskIndex] = '- [ ] **PARTIAL** — ' + $description + ' — done: ' + (Clean-Cell $Done) + '; remaining: ' + (Clean-Cell $Remaining)
                    $logEvidence = 'Done: ' + (Clean-Cell $Done) + '; remaining: ' + (Clean-Cell $Remaining)
                    $logNext = Clean-Cell $NextAction
                }
                'BLOCKED' {
                    $lines[$taskIndex] = '- [ ] **BLOCKED** — ' + $description + ' — reason: ' + (Clean-Cell $Evidence) + '; next: ' + (Clean-Cell $NextAction)
                    $logEvidence = 'Blocker: ' + (Clean-Cell $Evidence)
                    $logNext = Clean-Cell $NextAction
                }
            }

            $remainingWorking = @($lines | Where-Object { $_ -match '^\s*-\s\[\s\]\s+\*\*WORKING\*\*' })
            if ($remainingWorking.Count -gt 0) {
                throw "Another WORKING task remains. Resolve it before finishing: $($remainingWorking -join '; ')."
            }
            $logStatus = $Status
        }

        $headerIndex = -1
        for ($i = 0; $i -lt $lines.Count - 1; $i++) {
            if ($lines[$i] -match '^\|\s*Date\s*\|\s*Task / milestone\s*\|') {
                $headerIndex = $i
                break
            }
        }
        if ($headerIndex -lt 0 -or $lines[$headerIndex + 1] -notmatch '^\|[- :|]+\|$') {
            throw 'Execution Log table header was not found in the expected format. No file was written.'
        }

        if (-not [string]::IsNullOrWhiteSpace($StatusRowLabel)) {
            $statusRowIndices = @()
            $statusRowPattern = '^\|\s*' + [regex]::Escape($StatusRowLabel) + '\s*\|'
            for ($i = 0; $i -lt $lines.Count; $i++) {
                if ($lines[$i] -match $statusRowPattern) { $statusRowIndices += $i }
            }
            if ($statusRowIndices.Count -ne 1) {
                throw "Expected one status-table row labelled '$StatusRowLabel'; found $($statusRowIndices.Count). No file was written."
            }
            $statusCells = $lines[[int]$statusRowIndices[0]].Split('|')
            if ($statusCells.Count -lt 4) { throw 'The selected status-table row is malformed.' }
            $statusCells[2] = ' ' + $logStatus + ' '
            $lines[[int]$statusRowIndices[0]] = $statusCells -join '|'
        }

        $date = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
        $logTask = Clean-Cell $TaskText
        $row = '| ' + $date + ' | ' + $logTask + ' | ' + $logStatus + ' | ' + (Clean-Cell $logEvidence) + ' | ' + (Clean-Cell $logNext) + ' |'
        $before = @($lines[0..($headerIndex + 1)])
        $after = @()
        if ($headerIndex + 2 -lt $lines.Count) { $after = @($lines[($headerIndex + 2)..($lines.Count - 1)]) }
        $newLines = @($before) + @($row) + @($after)
        $newContent = ($newLines -join $newline).TrimEnd([char[]]@([char]13, [char]10)) + $newline

        if ($newContent -eq $content) { throw 'No effective change was generated.' }

        [IO.File]::WriteAllText($masterPath, $newContent, [System.Text.UTF8Encoding]::new($false))
        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'add', '--', 'MASTER_TODO.md'))

        $stagedNames = Invoke-BoundedGit $git @('-C', $repoRoot, 'diff', '--cached', '--name-only', '--', 'MASTER_TODO.md')
        if ($stagedNames.Trim() -ne 'MASTER_TODO.md') {
            throw 'The master checklist was not staged exactly as expected. No commit was made.'
        }

        $message = if ($Action -eq 'Start') { "JARVIS: start task - $TaskText" } else { "JARVIS: $($Status.ToLowerInvariant()) - $TaskText" }
        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'commit', '--only', '-m', $message, '--', 'MASTER_TODO.md'))

        Write-Host 'Pushing the single-file master checklist update...' -ForegroundColor Cyan
        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'push', 'origin', 'main'))

        [void](Invoke-BoundedGit $git @('-C', $repoRoot, 'fetch', '--no-tags', 'origin', 'main'))
        $remoteContent = Invoke-BoundedGit $git @('-C', $repoRoot, 'show', 'FETCH_HEAD:MASTER_TODO.md')
        $lf = [string][char]10
        $localNormalized = [regex]::Replace($newContent, '\r\n?', $lf)
        $remoteNormalized = [regex]::Replace($remoteContent, '\r\n?', $lf)
        if ($localNormalized -ne $remoteNormalized) {
            throw 'Remote read-back does not match the local master file. The local commit was retained for inspection; no reset was performed.'
        }

        Write-Host "SUCCESS: $Action update pushed and verified by remote read-back." -ForegroundColor Green
        Write-Host "Task: $TaskText"
        Write-Host "Status: $logStatus"
    }
    finally {
        $env:GIT_TERMINAL_PROMPT = $oldPrompt
        $env:GCM_INTERACTIVE = $oldGcm
    }
}
catch {
    Write-Error $_
    exit 1
}
