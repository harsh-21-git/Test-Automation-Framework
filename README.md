# Test Automation Framework

This project is a Selenium-based test automation framework developed in Python. It automates UI testing for web applications, supports cross-browser testing, and integrates easily with CI/CD pipelines.

## Features

- Selenium WebDriver integration
- Page Object Model (POM) design pattern
- Cross-browser support (Chrome, Firefox)
- HTML test reports
- Centralized configuration and utilities
- Easily extendable structure for large test suites

## Tools & Technologies

- Python
- Selenium
- PyTest
- HTMLTestRunner
- ChromeDriver / GeckoDriver

## Setup Instructions

1. Clone the repo:
   ```
   git clone <repo-url>
   cd test-automation-framework
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run tests:
   ```
   pytest --html=reports/report.html
   ```

## Sample Test Structure

- `pages/`: Page classes using POM
- `tests/`: Actual test cases
- `utils/`: Common utilities like config reader, logger
- `drivers/`: WebDriver setup
- `reports/`: Generated test reports

## Author

Harsh Arora
