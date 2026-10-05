[CmdletBinding()]
param(
    [string]$PythonPath,
    [string]$Diagram = 'all',
    [switch]$Check
)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$pythonPrefix = @()
if (-not $PythonPath) {
    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if ($launcher) { $PythonPath = $launcher.Source; $pythonPrefix = @('-3') }
    else {
        $python = Get-Command python -ErrorAction SilentlyContinue
        if (-not $python) { throw 'Python 3 is required. Supply -PythonPath with your Python executable path; see diagrams/README.md.' }
        $PythonPath = $python.Source
    }
}
$buildArgs = @((Join-Path $PSScriptRoot 'build_diagrams.py'), '--root', $repoRoot, '--diagram', $Diagram)
if ($Check) { $buildArgs += '--check' }
& $PythonPath @pythonPrefix @buildArgs
if ($LASTEXITCODE -ne 0) { throw "Diagram builder failed (exit $LASTEXITCODE). See diagrams/README.md for setup and validation." }
