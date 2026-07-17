param(
    [switch]$Release
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $RepoRoot

$previousBytecode = $env:PYTHONDONTWRITEBYTECODE
$env:PYTHONDONTWRITEBYTECODE = "1"

try {
    python -m unittest discover -s tests -p "test_*.py"
    if ($LASTEXITCODE -ne 0) { throw "Validator unit tests failed." }

    python scripts/check_showcase.py
    if ($LASTEXITCODE -ne 0) { throw "Base showcase validation failed." }

    if ($Release) {
        python scripts/check_release_candidate.py --release
    } else {
        python scripts/check_release_candidate.py
    }
    if ($LASTEXITCODE -ne 0) { throw "Release-candidate validation failed." }

    Write-Host "GymFlow local release validation completed successfully."
}
finally {
    if ($null -eq $previousBytecode) {
        Remove-Item Env:\PYTHONDONTWRITEBYTECODE -ErrorAction SilentlyContinue
    } else {
        $env:PYTHONDONTWRITEBYTECODE = $previousBytecode
    }
    Get-ChildItem -Path . -Directory -Filter "__pycache__" -Recurse -ErrorAction SilentlyContinue |
        Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Pop-Location
}
