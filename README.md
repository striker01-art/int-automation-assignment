# AI-Generated Test Case Builder + Script Execution (INT. Automation Assignment)

**Candidate:** Soumyadeep Mandal  
**Role:** Tech | Automation Testing (Indus Net Technologies Limited)  
**Target Application:** [https://www.saucedemo.com/](https://www.saucedemo.com/)  
**Tech Stack:** Python 3, Selenium WebDriver, Pytest, Page Object Model (POM)

## 1. AI-Generated Test Cases (Login Functionality)

| Test ID | Test Scenario | Test Data | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC-01** | Valid Login (Happy Path) | `standard_user` / `secret_sauce` | Redirected to `/inventory.html` displaying product catalog. |
| **TC-02** | Locked-Out User Restriction | `locked_out_user` / `secret_sauce` | Error banner: `Epic sadface: Sorry, this user has been locked out.` |
| **TC-03** | Invalid Password Authentication | `standard_user` / `wrong_password_123` | Error banner: `Epic sadface: Username and password do not match any user in this service` |
| **TC-04** | Empty Username Field Validation | `""` / `secret_sauce` | Error banner: `Epic sadface: Username is required` |
| **TC-05** | SQL Injection Input Boundary | `' OR '1'='1` / `secret_sauce` | Safely rejected with standard credential mismatch error. |

## 2. Reasoning: How AI Improved Test Design
- **Expanded Edge-Case Coverage:** AI surfaced account-state restrictions (`locked_out_user`) and security boundary inputs (`' OR '1'='1`) beyond standard valid/invalid checks.
- **Deterministic Assertions:** Standardized exact UI error strings (`[data-test='error']`) for unambiguous Pytest assertions.
- **Human-in-the-Loop Refactoring:** Structured locators into a reusable Page Object Model (`pages/login_page.py`) using explicit `WebDriverWait` conditions instead of brittle `time.sleep()` delays.

## 3. Setup & Execution Steps
```bash
git clone [https://github.com/striker01-art/int-automation-assignment.git](https://github.com/striker01-art/int-automation-assignment.git)
cd int-automation-assignment
pip install -r requirements.txt
pytest -v
```
