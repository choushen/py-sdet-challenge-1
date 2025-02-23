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

Create an automated test suite for **[Sweetshop](https://sweetshop.netlify.app/)** that includes:  

- [ ] User registration and login (use the greyed-out, pre-populated credentials)  
- [ ] Product browsing and search functionality  
- [ ] Shopping basket operations  
- [ ] Checkout process  
- [ ] Order history verification  

#### **Identified Test Cases**  

- [ ] Login with valid credentials  
- [ ] Login with invalid credentials  
- [ ] Add to Basket  
- [ ] Remove from Basket  
- [ ] Checkout  
- [ ] Order History  

### **Assumptions and Justifications**  

...  

### **Design**  

...  

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

## **Author**  

Jacob McKenzie
