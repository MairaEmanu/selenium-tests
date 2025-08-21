# Selenium Login Test Automation (Python)

This is a test automation project written in Python using Selenium WebDriver and PyTest.

The goal of this project is to automate a login flow on [SauceDemo](https://www.saucedemo.com) using the Page Object Model (POM) structure.  
It is part of my personal learning plan to become a Test Automation Engineer.

---

## 📂 Project Structure

```
selenium-tests/
├── pages/
│   ├── login_page.py 
│   └── base_page.py
├── tests/
│   └── test_login.py
├── requirements.txt
└── README.md
```

---

## Tools & Technologies

- Python 3.12.7
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Git & GitHub

---

## How to Run This Project

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Run the test:  
   ```bash
   pytest tests/test_login.py
   ```
> Make sure you have the correct version of ChromeDriver installed and in your system PATH.

---

## Learning Goals

- Apply Selenium with PyTest
- Structure tests using Page Object Model
- Learn how to use waits and element interaction
- Build a reusable and scalable UI test framework

---

## Status

✅ Login test completed using POM  
⬜ Add more test cases (e.g., invalid login, logout, cart flow)  
⬜ API tests (planned for week 3 of study plan)  

---

## Author

**Maira Emanuel**  
Aspiring Test Automation Engineer
