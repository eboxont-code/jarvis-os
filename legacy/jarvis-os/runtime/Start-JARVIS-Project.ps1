[CmdletBinding()]
param(
    [switch]$SyncOnly,
    [string]$AppPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Step([string]$Message) {
    Write-Host ("[{0}] {1}" -f (Get-Date -Format 'HH:mm:ss'), $Message) -ForegroundColor Cyan
}

function Invoke-BoundedProcess {
    param(
        [Parameter(Mandatory)][string]$FilePath,
        [Parameter(Mandatory)][string[]]$Arguments,
        [int]$TimeoutSeconds = 45
    )

    $quoted = foreach ($arg in $Arguments) {
        '"' + ([string]$arg).Replace('"', '\"') + '"'
    }

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $FilePath
    $psi.Arguments = ($quoted -join ' ')
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.StandardOutputEncoding = [Text.Encoding]::UTF8
    $psi.StandardErrorEncoding = [Text.Encoding]::UTF8

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $psi

    try {
        [void]$process.Start()
        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        if (-not $process.WaitForExit($TimeoutSeconds * 1000)) {
            try { $process.Kill() } catch {}
            throw "Timed out after $TimeoutSeconds seconds: $FilePath $($Arguments -join ' ')"
        }

        $process.WaitForExit()
        $stdout = $stdoutTask.GetAwaiter().GetResult()
        $stderr = $stderrTask.GetAwaiter().GetResult()

        if ($process.ExitCode -ne 0) {
            $detail = (($stdout, $stderr) -join [Environment]::NewLine).Trim()
            throw ("Command failed with exit code {0}: {1} {2}{3}{4}" -f $process.ExitCode, $FilePath, ($Arguments -join ' '), [Environment]::NewLine, $detail)
        }

        return $stdout.TrimEnd()
    }
    finally {
        $process.Dispose()
    }
}

function Get-RepositoryRoot {
    $candidate = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
    if (-not (Test-Path (Join-Path $candidate 'MASTER_TODO.md'))) {
        throw "MASTER_TODO.md not found beside the controller. Run this script from a clone of eboxont-code/jarvis-os."
    }
    return $candidate
}

function Sync-ProjectRepository([string]$RepoRoot) {
    $gitCommand = Get-Command git -ErrorAction Stop
    $git = $gitCommand.Source

    $oldTerminalPrompt = $env:GIT_TERMINAL_PROMPT
    $oldGcmInteractive = $env:GCM_INTERACTIVE
    $env:GIT_TERMINAL_PROMPT = '0'
    $env:GCM_INTERACTIVE = 'never'

    try {
        $branch = Invoke-BoundedProcess $git @('-C', $RepoRoot, 'branch', '--show-current')
        if ($branch.Trim() -ne 'main') {
            throw "Expected branch 'main'; current branch is '$branch'. No branch switch was attempted."
        }

        $origin = Invoke-BoundedProcess $git @('-C', $RepoRoot, 'remote', 'get-url', 'origin')
        if ($origin -notmatch '^(https://github\.com/eboxont-code/jarvis-os(?:\.git)?/?|git@github\.com:eboxont-code/jarvis-os(?:\.git)?)$') {
            throw "Unexpected origin remote '$origin'. Expected the private eboxont-code/jarvis-os repository."
        }

        $dirtyInstructions = Invoke-BoundedProcess $git @('-C', $RepoRoot, 'status', '--porcelain', '--', 'AGENTS.md', 'MASTER_TODO.md')
        if (-not [string]::IsNullOrWhiteSpace($dirtyInstructions)) {
            throw "AGENTS.md or MASTER_TODO.md has local edits. The controller will not overwrite them. Commit or safely resolve those edits first."
        }

        Write-Step 'Fetching the latest private JARVIS master files...'
        [void](Invoke-BoundedProcess $git @('-C', $RepoRoot, 'fetch', '--no-tags', 'origin', 'main'))

        Write-Step 'Applying only a fast-forward update...'
        [void](Invoke-BoundedProcess $git @('-C', $RepoRoot, 'merge', '--ff-only', 'FETCH_HEAD'))

        $head = Invoke-BoundedProcess $git @('-C', $RepoRoot, 'rev-parse', 'HEAD')
        $remoteHead = Invoke-BoundedProcess $git @('-C', $RepoRoot, 'rev-parse', 'FETCH_HEAD')
        if ($head.Trim() -ne $remoteHead.Trim()) {
            throw 'Local main did not reach the fetched remote commit. No reset or forced update was attempted.'
        }

        return [pscustomobject]@{ Git = $git; Head = $head.Trim() }
    }
    finally {
        $env:GIT_TERMINAL_PROMPT = $oldTerminalPrompt
        $env:GCM_INTERACTIVE = $oldGcmInteractive
    }
}

function Get-OpenJarvisConfigPath {
    if (-not [string]::IsNullOrWhiteSpace($env:OPENJARVIS_CONFIG)) {
        return [Environment]::ExpandEnvironmentVariables($env:OPENJARVIS_CONFIG)
    }

    if (-not [string]::IsNullOrWhiteSpace($env:OPENJARVIS_HOME)) {
        $homePath = [Environment]::ExpandEnvironmentVariables($env:OPENJARVIS_HOME)
        return Join-Path $homePath 'config.toml'
    }

    return Join-Path $HOME '.openjarvis\config.toml'
}

function Update-OpenJarvisProjectPrompt {
    param(
        [string]$RepoRoot,
        [string]$Commit
    )

    $configPath = Get-OpenJarvisConfigPath
    if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) {
        throw "OpenJarvis config not found at '$configPath'. No new config was created. Confirm the active path with the installed OpenJarvis config-path command."
    }

    $configDirectory = Split-Path -Parent $configPath
    $projectDirectory = Join-Path $configDirectory 'jarvis-os'
    [void](New-Item -ItemType Directory -Path $projectDirectory -Force)

    $agentsPath = Join-Path $RepoRoot 'AGENTS.md'
    $masterPath = Join-Path $RepoRoot 'MASTER_TODO.md'
    $agents = [IO.File]::ReadAllText($agentsPath, [Text.Encoding]::UTF8)
    $master = [IO.File]::ReadAllText($masterPath, [Text.Encoding]::UTF8)

    if ([string]::IsNullOrWhiteSpace($agents) -or [string]::IsNullOrWhiteSpace($master)) {
        throw 'AGENTS.md or MASTER_TODO.md is empty; prompt generation was stopped.'
    }

    $promptPath = Join-Path $projectDirectory 'JARVIS_PROJECT_SYSTEM_PROMPT.md'
    $prompt = @"
# JARVIS project session context

This file is generated by the local JARVIS Project Controller from the latest private repository checkout.
Repository: eboxont-code/jarvis-os
Branch: main
Commit: $Commit
Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss K')

The complete authoritative project instructions and master checklist follow.
Treat these project files as the controlling project context. Do not claim that a Windows action was performed unless it was actually executed and verified.

---

# AGENTS.md

$agents

---

# MASTER_TODO.md

$master
"@

    $promptTemp = "$promptPath.tmp"
    [IO.File]::WriteAllText($promptTemp, $prompt, [System.Text.UTF8Encoding]::new($false))
    Move-Item -LiteralPath $promptTemp -Destination $promptPath -Force

    $configText = [IO.File]::ReadAllText($configPath, [Text.Encoding]::UTF8)
    $newline = [Environment]::NewLine
    $lines = New-Object 'System.Collections.Generic.List[string]'
    foreach ($line in ($configText -split '\r?\n')) { [void]$lines.Add($line) }

    $agentStart = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match '^\s*\[agent\]\s*(?:#.*)?$') {
            $agentStart = $i
            break
        }
    }

    if ($agentStart -lt 0) {
        if ($lines.Count -gt 0 -and -not [string]::IsNullOrWhiteSpace($lines[$lines.Count - 1])) {
            [void]$lines.Add('')
        }
        [void]$lines.Add('[agent]')
        [void]$lines.Add('system_prompt_path = "' + ($promptPath -replace '\\', '/') + '"')
    }
    else {
        $agentEnd = $lines.Count
        for ($i = $agentStart + 1; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match '^\s*\[[^\]]+\]\s*(?:#.*)?$') {
                $agentEnd = $i
                break
            }
        }

        $pathLineIndex = -1
        $pathLineCount = 0

        for ($i = $agentStart + 1; $i -lt $agentEnd; $i++) {
            $line = $lines[$i]

            if ($line -match '^\s*system_prompt\s*=') {
                $rhs = (($line -replace '\s+#.*$', '') -split '=', 2)[1].Trim()
                if ($rhs -ne '""' -and $rhs -ne "''") {
                    throw 'The existing [agent].system_prompt is non-empty and takes precedence over system_prompt_path. It was preserved. Merge it manually before enabling the project prompt.'
                }
            }

            if ($line -match '^\s*system_prompt_path\s*=') {
                $pathLineCount++
                $pathLineIndex = $i
                $rhs = (($line -replace '\s+#.*$', '') -split '=', 2)[1].Trim()
                $existingValue = $rhs.Trim('"').Trim("'")
                $expectedValue = $promptPath -replace '\\', '/'
                if (-not [string]::IsNullOrWhiteSpace($existingValue) -and $existingValue -ne $expectedValue -and $existingValue -ne $promptPath) {
                    throw "The existing [agent].system_prompt_path points to '$existingValue'. It was preserved; review and merge that prompt before continuing."
                }
            }
        }

        if ($pathLineCount -gt 1) {
            throw 'Multiple system_prompt_path settings were found in [agent]. No config change was made.'
        }

        $setting = 'system_prompt_path = "' + ($promptPath -replace '\\', '/') + '"'
        if ($pathLineIndex -ge 0) {
            $lines[$pathLineIndex] = $setting
        }
        else {
            $lines.Insert($agentEnd, $setting)
        }
    }

    $newConfig = ($lines -join $newline).TrimEnd([char[]]@([char]13, [char]10)) + $newline
    if ($newConfig -ne $configText) {
        $backupPath = "$configPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
        Copy-Item -LiteralPath $configPath -Destination $backupPath
        $configTemp = "$configPath.tmp"
        [IO.File]::WriteAllText($configTemp, $newConfig, [System.Text.UTF8Encoding]::new($false))
        Move-Item -LiteralPath $configTemp -Destination $configPath -Force
        Write-Step "Updated OpenJarvis config. Backup: $backupPath"
    }
    else {
        Write-Step 'OpenJarvis config already points to the generated JARVIS project prompt.'
    }

    $verifyConfig = [IO.File]::ReadAllText($configPath, [Text.Encoding]::UTF8)
    $expected = 'system_prompt_path = "' + ($promptPath -replace '\\', '/') + '"'
    if (-not $verifyConfig.Contains($expected) -or -not (Test-Path -LiteralPath $promptPath -PathType Leaf)) {
        throw 'Config or generated prompt read-back verification failed.'
    }

    $verifyPrompt = [IO.File]::ReadAllText($promptPath, [Text.Encoding]::UTF8)
    if (-not $verifyPrompt.Contains('# MASTER_TODO.md') -or -not $verifyPrompt.Contains('# AGENTS.md')) {
        throw 'Generated prompt is missing one of the authoritative project files.'
    }

    return [pscustomobject]@{ ConfigPath = $configPath; PromptPath = $promptPath }
}

function Start-OpenJarvis {
    $running = @(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -match 'OpenJarvis|Jarvis' })
    if ($running.Count -gt 0) {
        Write-Warning 'OpenJarvis appears to be running. The controller did not close it or relaunch over it. Close OpenJarvis fully, then run the JARVIS Project Session shortcut again.'
        return
    }

    if (-not [string]::IsNullOrWhiteSpace($AppPath)) {
        if (-not (Test-Path -LiteralPath $AppPath -PathType Leaf)) {
            throw "The supplied OpenJarvis application path does not exist: $AppPath"
        }
        Start-Process -FilePath $AppPath
        Write-Step 'Launched OpenJarvis using the supplied executable path.'
        return
    }

    $startApps = @()
    if (Get-Command Get-StartApps -ErrorAction SilentlyContinue) {
        $startApps = @(Get-StartApps | Where-Object { $_.Name -match 'Open\s*Jarvis' })
    }

    if ($startApps.Count -eq 1) {
        Start-Process -FilePath "$env:SystemRoot\explorer.exe" -ArgumentList "shell:AppsFolder\$($startApps[0].AppID)"
        Write-Step "Launched Start-menu app '$($startApps[0].Name)'."
        return
    }

    $shortcutRoots = @(
        (Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs'),
        (Join-Path $env:ProgramData 'Microsoft\Windows\Start Menu\Programs')
    ) | Where-Object { Test-Path -LiteralPath $_ }

    $shortcuts = @()
    foreach ($root in $shortcutRoots) {
        $shortcuts += @(Get-ChildItem -LiteralPath $root -Filter '*.lnk' -File -Recurse -ErrorAction SilentlyContinue |
            Where-Object { $_.BaseName -match 'Open\s*Jarvis' })
    }

    if ($startApps.Count -gt 1 -or $shortcuts.Count -gt 1) {
        Write-Warning 'Multiple OpenJarvis shortcuts were found. Sync completed, but no app was launched automatically. Open the correct app manually.'
    }
    elseif ($shortcuts.Count -eq 1) {
        Start-Process -FilePath $shortcuts[0].FullName
        Write-Step "Launched OpenJarvis from '$($shortcuts[0].FullName)'."
    }
    else {
        Write-Warning 'No unique OpenJarvis Start-menu entry was found. Sync completed; open the installed app manually. You can rerun with -AppPath "C:\path\OpenJarvis.exe".'
    }
}

try {
    Write-Step 'Starting JARVIS project session bootstrap.'
    $repoRoot = Get-RepositoryRoot
    $sync = Sync-ProjectRepository $repoRoot
    Write-Step "Repository is current at commit $($sync.Head)."

    $paths = Update-OpenJarvisProjectPrompt -RepoRoot $repoRoot -Commit $sync.Head
    Write-Step "Generated prompt: $($paths.PromptPath)"
    Write-Step "OpenJarvis config: $($paths.ConfigPath)"
    Write-Step 'The full AGENTS.md and latest MASTER_TODO.md have been read back into the configured prompt.'

    if (-not $SyncOnly) {
        Start-OpenJarvis
    }

    Write-Host 'JARVIS project bootstrap completed. The OpenJarvis runtime still needs its first end-to-end prompt-load test.' -ForegroundColor Green
}
catch {
    Write-Error $_
    exit 1
}
