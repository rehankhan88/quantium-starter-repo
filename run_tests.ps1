# Exit on error
$ErrorActionPreference = "Stop"

# Activate virtual environment
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    . .\venv\Scripts\Activate.ps1
} else {
    Write-Error "Virtual environment not found!"
    exit 1
}

# Run tests
pytest test_app.py
$TEST_EXIT_CODE = $LASTEXITCODE

# Exit with proper code
if ($TEST_EXIT_CODE -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Host "Some tests failed!"
    exit 1
}
