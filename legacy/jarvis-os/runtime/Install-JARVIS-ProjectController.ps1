[CmdletBinding()]
param(
    [string]$AppPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

try {
    $repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
    $launcher = Join-Path $PSScriptRoot 'Start-JARVIS-Project.ps1'
    $statusTool = Join-Path $PSScriptRoot 'Update-JARVIS-TaskStatus.ps1'

    foreach ($path in @($launcher, $statusTool, (Join-Path $repoRoot 'AGENTS.md'), (Join-Path $repoRoot 'MASTER_TODO.md'))) {
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required controller file is missing: $path"
        }
    }

    Write-Host '[1/4] Checking PowerShell syntax...' -ForegroundColor Cyan
    foreach ($path in @($launcher, $statusTool, $PSCommandPath)) {
        $tokens = $null
        $parseErrors = $null
        [void][System.Management.Automation.Language.Parser]::ParseFile($path, [ref]$tokens, [ref]$parseErrors)
        if ($parseErrors.Count -gt 0) {
            $details = ($parseErrors | ForEach-Object { $_.Message }) -join '; '
            throw "PowerShell syntax check failed for '$path': $details"
        }
    }

    Write-Host '[2/4] Creating the desktop session shortcut...' -ForegroundColor Cyan
    $desktop = [Environment]::GetFolderPath('Desktop')
    $shortcutPath = Join-Path $desktop 'JARVIS Project Session.lnk'
    $powershellExe = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'

    if (-not (Test-Path -LiteralPath $powershellExe -PathType Leaf)) {
        throw "Windows PowerShell was not found at '$powershellExe'."
    }

    $shell = New-Object -ComObject WScript.Shell
    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = $powershellExe
    $shortcutArguments = '-NoLogo -NoProfile -ExecutionPolicy Bypass -File "' + $launcher + '"'
    if (-not [string]::IsNullOrWhiteSpace($AppPath)) {
        $shortcutArguments += ' -AppPath "' + $AppPath.Replace('"', '"') + '"'
    }
    $shortcut.Arguments = $shortcutArguments
    $shortcut.WorkingDirectory = $repoRoot
    $shortcut.Description = 'Refreshes the private JARVIS master plan and starts an OpenJarvis project session.'
    $shortcut.Save()

    Write-Host '[3/4] Running the first private-repository sync and OpenJarvis config setup...' -ForegroundColor Cyan
    if ([string]::IsNullOrWhiteSpace($AppPath)) {
        & $launcher -SyncOnly
    }
    else {
        & $launcher -SyncOnly -AppPath $AppPath
    }

    Write-Host '[4/4] Installation completed.' -ForegroundColor Green
    Write-Host "Desktop shortcut: $shortcutPath"
    Write-Host 'Use the "JARVIS Project Session" shortcut for each project session so the private master files refresh before OpenJarvis starts.'
    Write-Host 'The first actual OpenJarvis prompt-load test is still required; this script does not claim that the desktop runtime has passed it.'
}
catch {
    Write-Error $_
    exit 1
}
