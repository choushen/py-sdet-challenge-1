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

### **Assumptions and Justifications**  

...  

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

### **Prerequisites**

- Visual Studio Code
- Python 3.13
- Pip 25.0  
- Docker  
- Docker Compose  
- Git  

### **Installation**

1. Clone the repository to your local machine using the following command:  

```bash
git clone git@github.com:choushen/py-sdet-challenge-1.git
```

2. Navigate to the root of the project and create a virtual environment using the following command:

```bash
python -m venv venv
```  

3. Activate the virtual environment using the following command:  

#### **Windows**  

```bash
.\venv\Scripts\activate
```

#### **Linux/Mac**  

```bash
source venv/bin/activate
```

4. Install the project dependencies using the following command:  

```bash
pip install -r requirements.txt
```

### **Running the Test Suite**

To run the test suite, you can use the following command:  

```bash
pytest tests
```

## **Trouble Shooting Guide**

Any issues common issues you may encounter/what I encountered and how I resolved them will be included in this section of the document.

### **Issue 1** Running the test suite in VSCode

Ensure that you create a .vscode folder in the root of the project and add a settings.json file with the following content:

```json

{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}

```

### Final note

If after following the setup instructions you encounter any issues, please go to the **[author](#author)** section of this document and reach out to me with any questions you might have.

## Future Considerations

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

## **Author**  

**Name:** Jacob McKenzie
**Email:** jacob.mckenzie@icloud.com
