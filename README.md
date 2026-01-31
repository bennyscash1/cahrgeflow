
הנושאים העיקריים בתיקייה
בדיקות אוטומטיות (Pywright) לאתר מציגות 10 בדיקות עברו ומתמקדות בתרחישי כניסה ותאימות לדפדפנים.

# PyAutomationPlayRight

## Overview
PyAutomationPlayRight is an automated testing framework using Playwright for web testing with pytest.

## Project Structure
```
WebTest/
├── Flows/              # Test workflows
├── PageObject/         # Page Object Model
├── Test/               # Test cases
│   ├── CompatibilityTest/
│   ├── DashboardTest/
│   ├── InvalidLogin/
│   └── LoginTest/
└── WebInfra/          # Web driver and locator utilities

CommonInfra/           # Common infrastructure
TestResult/            # Test reports output
```

## Running Tests

### Run All Tests
```powershell
python -m pytest
```

### Run Tests with HTML Report (Timestamped)
Generate an HTML report with a timestamped filename in the `TestResult` directory:

```powershell
python -m pytest --html="TestResult/report_$(Get-Date -Format 'yyyyMMdd_HHmmss').html" --self-contained-html
```

**Options:**
- `--html`: Specifies the output path for the HTML report
- `--self-contained-html`: Embeds all CSS and JavaScript in the HTML file (no external dependencies)
- Report location: `TestResult/report_<YYYYMMDD_HHmmss>.html`

**Example Output:**
```
Generated html report: {Root}//PyAutoChargeFlow/TestResult/report_20260130_101515.html
```

### Run a Single Test File
Run all tests in a specific test file:

```powershell
python -m pytest WebTest/Test/LoginTest/test_valid_login.py
```

### Run a Single Test Function
Run a specific test function:

```powershell
python -m pytest WebTest/Test/LoginTest/test_valid_login.py::test_login_with_valid_credentials
```

### Run Tests by Pattern/Marker
Run tests matching a specific pattern:

```powershell
python -m pytest -k "login" --html="TestResult/report_$(Get-Date -Format 'yyyyMMdd_HHmmss').html" --self-contained-html
```

### Run Tests with Verbose Output
```powershell
python -m pytest -v
```

### Run Tests and Show Print Statements
```powershell
python -m pytest -s
```

### Run Tests in Parallel
Run tests concurrently to speed up execution (requires `pytest-xdist`):

```powershell
python -m pytest -n auto
```

**Options:**
- `-n auto`: Uses all available CPU cores
- `-n 4`: Uses 4 workers (specify number as needed)
- `--dist loadscope`: Distributes tests by scope (class/module)

**Example with HTML Report:**
```powershell run parrallel all tests with report
python -m pytest -n auto --html="TestResult/report_$(Get-Date -Format 'yyyyMMdd_HHmmss').html" --self-contained-html
```

### Combining Options
Run a single test with verbose output and HTML report:

```powershell
python -m pytest WebTest/Test/LoginTest/test_valid_login.py -v --html="TestResult/report_$(Get-Date -Format 'yyyyMMdd_HHmmss').html" --self-contained-html
```

## Common pytest Commands Reference

| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests |
| `pytest file.py` | Run tests in a specific file |
| `pytest file.py::test_func` | Run a specific test function |
| `pytest -k "pattern"` | Run tests matching a pattern |
| `pytest -v` | Verbose output |
| `pytest -s` | Show print statements |
| `pytest --html=report.html --self-contained-html` | Generate HTML report |
| `pytest -m "marker_name"` | Run tests with specific marker |
| `pytest --co` | List all available tests |

## Requirements
See `requirements.txt` for all dependencies:
- pytest
- pytest-html
- playwright
- Appium-Python-Client
- requests
