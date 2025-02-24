# **Challenge 1 - UI Automation Testing - Sweetshop**  

The challenge is to create and containerize a test automation framework for the **Sweetshop** application.  

## **Task & Requirements**  

### **Requirements**  

#### **Framework Requirements**  

- Use Python with Selenium WebDriver  
- Implement a standard design pattern  
- Implement comprehensive test coverage  
- Use a data-driven approach  
- Implement reporting
  - Pytest HTML report

#### **Standards and Code Quality**  

- Add test documentation  
- Project setup instructions  
- Test execution guidelines  
- Environment configuration  
- Troubleshooting guide  
- Follow PEP 8 standards  

### **Task**  

Create an automated test suite for **[Sweetshop](https://sweetshop.netlify.app/)** 

#### **Identified Test Cases**  

- [x] Login with valid credentials  
- [x] Login with invalid credentials  
- [ ] Add to Basket  
- [ ] Remove from Basket  
- [ ] Edit Basket
- [ ] Checkout  
- [ ] Order History  

### **Design**  

- **Page Object Model**
  - Each page will have its own class  
  - Each class will contain the locators and methods for the page

- **Driver Factory**
  - Will be used to create the driver instance  

- **Data Driven Approach**
  - Will use a JSON file to store test data
  - Will use a .env file to store environment variables

## **Setup Instructions**  

Since you are pulling this repository, I'm going to assume you are familiar with Git and have it installed on your machine. If not, you can download it **[here](https://git-scm.com/downloads)**.  

You will also need a couple of other things installed on your machine. See below for the prerequisites.  

### **Running the Test Suite Locally**  

## **Prerequisites**  

Before running the tests, ensure you have the following installed:  

- Python 3.13+  
- Pip 25.0+  
- Google Chrome (for Selenium tests)  
- ChromeDriver (or use `webdriver-manager`, installed automatically)  

## **Running the Tests**  

1. Activate the virtual environment.  

#### **Windows (PowerShell or CMD)**  

```bash
.\venv\Scripts\activate
```

#### **Linux/Mac**  

```bash
source venv/bin/activate
```

2. Install dependencies.  

```bash
pip install -r requirements.txt
```

3. Set up environment variables.  

Open the **secrets_pt_1**  folder and extract the **.env** file. Place it in the root of the project. 

3b. Add the data files

Open the **secrets_pt_1.zip**  folder and drop the **resources** folder in the root of the project.

4. Run the Selenium test suite.  

Run all tests:  

```bash
pytest tests --html=reports/selenium_report.html
```

Run a specific test file:  

```bash
pytest tests/test_login.py --html=reports/login_report.html
```

Run tests in headless mode (no browser UI):

```bash
pytest tests --html=reports/selenium_report.html --headless
```

5. View test reports.  

#### **Windows (PowerShell)**

```powershell
Start-Process reports\selenium_report.html
```

#### **macOS/Linux**

```bash
open reports/selenium_report.html
```

## **Troubleshooting Guide**  

### **Running pytest returns "command not found"**  

Ensure the virtual environment is activated before running tests.  

```bash
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

If `pytest` is still missing, reinstall dependencies:  

```bash
pip install -r requirements.txt
```

### **Test reports are not generated**  

Ensure the `reports/` folder exists before running tests:  

```bash
mkdir -p reports
```

Then rerun:  

```bash
pytest tests --html=reports/selenium_report.html
```

### **Environment variables not loading**  

Ensure `.env` exists and is loaded correctly. To verify:  

```bash
python -c "import os; print(os.getenv('BASE_URL'))"
```

### **VS Code does not discover tests**  

Add this configuration to `.vscode/settings.json`:  

```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

Then restart VS Code.

### Final note

If after following the setup instructions you encounter any issues, please go to the **[author](#author)** section of this document and reach out to me with any questions you might have.

## Future Considerations

### General Improvements

- Comprehensive logging
- Implementing a test data management system (e.g. Test Database/API)
- Use pydantic for data validation
  - Include more logging in the data_reader utility
- Shorter docstrings for PEP 8 compliance
- Include supprot for other browsers such as Firefox, Safari, and Edge in the driver factory
- Implement allure reporting for better reporting (e.g. screenshots, videos, etc.)
- Implement a CI (e.g. Jenkins, GitHub Actions)
- Revise the project structure
- Containerise the test suite

### Non-Functional Requirements

- WCAG Compliance (e.g. axe-core)
- Cross-Browser Testing
- Device resolution testing
- Track metrics and check console logs
- Measure response times to ensure speed and reliability

## **Author**  

- **Name:** Jacob McKenzie
- **Email:** jacob.mckenzie@icloud.com
