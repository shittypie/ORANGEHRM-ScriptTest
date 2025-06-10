# ORANGEHRM-ScriptTest

**ORANGEHRM Script Test** is an automated end-to-end (E2E) testing project built with **Python** using **Selenium WebDriver** to test the core functionalities of the OrangeHRM web application. It simulates real user interactions to ensure that the HR system operates correctly across modules such as login, employee management, leave requests, and admin tasks.

This testing script is ideal for verifying the reliability and robustness of the OrangeHRM system in a continuous integration or QA environment.

🌐 **Test Site:**  
[https://opensource-demo.orangehrmlive.com/web/index.php/auth/login](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

📚 **More about OrangeHRM:**  
[https://sourceforge.net/projects/orangehrm/](https://sourceforge.net/projects/orangehrm/)

---

## ✅ E2E Testing Plan

Below is a breakdown of the E2E test cases implemented in the automation suite:

| Module           | Test Case ID | Test Case             | Test Objective                                                                 | Precondition                                                              | Expected Result                                                                 |
|------------------|--------------|------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Login Page**   | TC01         | Login Page             | 🔐 Verify login functionality and secure authentication                       | Valid user credentials are available                                      | User logs in successfully and is redirected to the dashboard                    |
| **PIM Module**   | TC02         | Add Employee           | 👤 Add a new employee with all required data                                  | Logged in as admin/HR                                                     | Employee added and appears in the employee list                                 |
|                  | TC03         | Add Personal Details   | ✏️ Enter and update employee personal details                                 | Employee profile exists                                                   | Details saved accurately and shown in profile                                   |
|                  | TC04         | Add Contact Details    | ☎️ Add and save employee contact information                                  | Employee profile exists                                                   | Contact info saved and displayed correctly                                      |
|                  | TC05         | Add Emergency Contacts | 🚨 Add emergency contact linked to employee                                   | Employee profile is editable                                              | Contact saved and linked properly                                               |
|                  | TC06         | Add Dependents         | 👶 Add dependents for employee                                                 | Employee profile exists                                                   | Dependents listed correctly in profile                                          |
|                  | TC07         | Add Immigration        | 🛂 Enter and track immigration records                                         | Employee must exist                                                       | Immigration data saved and retrievable                                          |
|                  | TC08         | Add Job                | 💼 Add job title and employment status                                        | Employee profile accessible                                               | Job info saved and visible in profile                                           |
|                  | TC09         | Add Salary             | 💵 Input salary details and validate records                                  | Employee profile accessible                                               | Salary data saved and linked to profile                                         |
|                  | TC10         | Add Tax Exemptions     | 🧾 Capture employee tax exemption info                                        | Employee profile accessible                                               | Tax exemptions stored correctly                                                 |
|                  | TC11         | Add Report To          | 🧑‍💼 Assign a supervisor or reporting manager                                  | Profile accessible for updates                                            | Reporting structure saved accurately                                            |
|                  | TC12         | Add Work Experience    | 📄 Record previous work experience                                            | Profile accessible                                                        | Experience entries saved and listed                                             |
|                  | TC13         | Add Membership         | 🏷️ Add memberships for the employee                                           | Profile accessible                                                        | Memberships stored and shown in profile                                         |
|                  | TC14         | System Search          | 🔎 Search and retrieve employee records                                       | Search field and data available                                           | Accurate records returned                                                        |
|                  | TC15         | Edit Details           | 📝 Edit and update existing employee details                                  | Employee profile exists                                                   | Changes saved and reflected                                                     |
|                  | TC16         | Delete Employee        | ❌ Remove an employee from the system                                         | Admin permission and employee exists                                      | Employee deleted and removed from results                                       |
| **Leave Module** | TC17         | Apply Leave            | 🌴 Submit a leave application                                                 | Active employee login                                                     | Leave application submitted with confirmation                                   |
|                  | TC18         | Leave Period           | 📆 Check if leave period settings are enforced                                | Leave periods pre-configured                                              | Leave allowed within defined timeframe                                          |
|                  | TC19         | Leave Types            | 🗂️ Verify availability and functionality of leave types                      | Leave types must be available                                             | Proper display and selection of leave types                                     |
|                  | TC20         | Configure Leave Period | ⚙️ Set up leave cycles                                                        | Admin access to config                                                    | Leave periods configured correctly                                              |
|                  | TC21         | Add Entitlements       | 📋 Add leave entitlements and validate calculations                           | Employee exists                                                           | Entitlements added and calculated                                               |
|                  | TC22         | Assign Leave           | 🧾 Assign leave to employees                                                  | Employee with valid leave type                                            | Leave assignment reflected in balance                                           |
|                  | TC23         | Generate Leave Report  | 📊 Generate report for leave activities                                       | Permission to access reports                                              | Accurate report generated                                                       |
|                  | TC24         | Add Holiday            | 📅 Add public holidays to the calendar                                        | Logged in with proper access                                              | Holiday appears in system calendar                                              |
|                  | TC25         | Edit Holiday           | 🧮 Update existing holiday entries                                            | Holiday exists                                                            | Updated holiday saved and reflected                                             |
|                  | TC26         | Delete Holiday         | 🗑️ Remove holidays from calendar                                              | Holiday exists                                                            | Holiday deleted from calendar                                                   |
| **Admin Module** | TC27         | Add Admin              | 🛠️ Create a new admin with proper roles                                       | Admin privileges required                                                 | Admin account created with roles                                                |
|                  | TC28         | Add Account            | ➕ Add user accounts with validations                                          | Logged in as admin                                                        | Account created and listed                                                      |
|                  | TC29         | Edit Account           | ✍️ Update existing account info                                               | Existing account info required                                            | Account info updated correctly                                                  |
|                  | TC30         | Search Account         | 🔍 Search for existing accounts                                               | Account records present                                                   | Search returns relevant account data                                            |
|                  | TC31         | Remove Admin           | ❎ Remove admin securely                                                       | Admin account exists                                                      | Admin deleted and access revoked                                                |
|                  | TC32         | Admin Logout           | 🔓 Verify logout functionality                                                | Admin logged in                                                           | Successfully logged out and redirected to login page                           |

---

## ⚠️ Notes

> 🚧 This project is **under development**, and some test functionalities may still have errors due to the **open-source nature** of OrangeHRM. Components of the system may be changed or modified by the community, which can impact the stability or behavior of automated tests.  
>
> 💡 Future updates will include more test cases, better error handling, and reporting features.

---

## 🛠 Tech Stack

- Python 🐍  
- Selenium WebDriver 🌐  
- PyTest or unittest for test execution  
- ChromeDriver for browser automation  

---

Feel free to fork this repo, contribute, or use it as a boilerplate for your own E2E testing projects.
