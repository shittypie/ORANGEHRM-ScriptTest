from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Library.clearFields import textfield

class AccountManagement:
    def __init__(self, driver):
        self.driver = driver

    def AddEmployee(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Juan")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Dela")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Cruz")
        time.sleep(2)
        empId = self.driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        empId.send_keys(Keys.CLEAR)
        time.sleep(1)
        empId.send_keys("51")
        
        # elem = WebDriverWait(self.driver, 5).until( # Enable Create Login Details
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-switch-input.oxd-switch-input--active.--label-right"))
        # )
        # self.driver.execute_script("arguments[0].click();", elem)
        
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("juan12345") # Username
        # # Enable or disable to make an account (Optional) Status of the account
        # # self.driver.find_element(By.XPATH, "//label[normalize-space()='Enabled']").click()
        # # self.driver.find_element(By.XPATH, "//label[normalize-space()='Disabled']").click()
        
        # self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("juan12345") # Password
        # self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("juan12345") # Confirm Password
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click() 
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def add_personalDetails(self): # Personal Details/Personal Details
        # Personal Details Section
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'Nickname')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Makoo") 
        time.sleep(5)
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'Employee Id')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("23") # ID
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'Other Id')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Student ID") # Other ID (Optional)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'License Number')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("123") # Driver's license no (Optional)
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'License Expiry Date')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("2025-12-12") # license Expiry Date
        # time.sleep(2)
        # try: # Nationality
        #     dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
        #     dropdown[0].click()
        #     options_xpath = "//div[@role='option']"
        #     options = WebDriverWait(self.driver, 5).until(
        #         EC.presence_of_all_elements_located((By.XPATH, options_xpath))
        #     )
        #     next(option for option in options if option.text.strip() == "Australian").click()
        # except Exception as e:
        #     print(f"An error occurred: {e}")
            
        # time.sleep(2)
        # try: # Marital Status
        #     dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
        #     dropdown[1].click()
        #     options_xpath = "//div[@role='option']"
        #     options = WebDriverWait(self.driver, 5).until(
        #         EC.presence_of_all_elements_located((By.XPATH, options_xpath))
        #     )
        #     next(option for option in options if option.text.strip() == "Single").click()
        # except Exception as e:
        #     print(f"An error occurred: {e}")
        
        # self.driver.find_element(By.XPATH, "//label[contains(text(), 'Date of Birth')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("2000-12-12") # Birthday
        
        # mGender = "//label[normalize-space()='Male']"
        # fGender = "//label[normalize-space()='Female']"
        # self.driver.find_element(By.XPATH, mGender).click()
        # self.driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]").click() # Save button 1
        
        # Custom Fields
        time.sleep(2)
        try: # Blood Type
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
            dropdown[1].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "A+").click()
        except Exception as e:
            print(f"An error occurred: {e}")
        
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Test_Field')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("none")
        self.driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[2]").click() # Save button 1
        
        # Attachment section
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--active'])[1]").click()
        
        time.sleep(2)
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        docfile = r"C:\Users\Mark Roel Andaya\Downloads\hey.txt"
        file_input.send_keys(docfile)
        print("file imported")
        
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]").send_keys("Comment")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    def add_contactDetails(self): # Personal Details/Contacts Details
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//a[normalize-space()=' Emergency Contacts'])[1]").click()
        # Address Section
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Street 1')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Street 2')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'City')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("City")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'State/Province')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Zip/Postal Code')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("1111")
        
        time.sleep(2)
        try: # Country
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Algeria").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")

        # Telephone Section
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Home')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("12345678") # Home
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Mobile')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("12345678") # Mobile
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Work')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("12345678") # Work
        
        # Email Section
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Work Email')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("sad@das.xyz") # Email
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Other Email')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("sad@gmail.com") # Other Email
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click() # Save button
        
    def emergencyContacts(self): # Personal Details/Emergency Contacts
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Emergency Contacts'])[1]").click()
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]").click() # Assigned emergency contacts
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Name')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Name")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Relationship')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Relationship")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Home Telephone')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Home Tel")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Mobile')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Mobile")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Work Telephone')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Work Tel")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        # driver.find_element(By.XPATH, '(//button[normalize-space()='Cancel'])[1]').click() # Cancel button
        
        # Attachment section
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--active'])[1]").click()
        
        time.sleep(2)
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        docfile = ""
        file_input.send_keys(docfile)
        
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]").send_keys("Comment")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[2]").click()
        # driver.find_element(By.XPATH, '(//button[normalize-space()='Cancel'])[2]').click() # Cancel button
        
    def dependents(self):  # Personal Details/Dependents
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Dependents'])[1]").click()
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]").click() # Assigned emergency contacts
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Name')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("Name")
        
        try: # Relationship
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Child").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Date of Birth')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("yyyy-mm-dd")
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        
        # Attachment section
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--active'])[1]").click()
        
        time.sleep(2)
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        docfile = ""
        file_input.send_keys(docfile)
        
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]").send_keys("Comment")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        
    def Immigration(self):  # Personal Details/Immigration
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Immigration'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]").click() # Assigned Immigration Records
        
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Passport']").click()
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Visa']").click() 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Number')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Issued Date')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Expiry Date')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Eligible Status')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        
        try: # Country
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Algeria").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        self.driver.find_element(By.XPATH, "//label[contains(text(), 'Eligible Review Date')]/following::input[@class='oxd-input oxd-input--active'][1]").send_keys("")
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Type Comments here']").send_keys("")
        
        self.driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]").click()
        
        # Attachment section
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]").click()
        self.driver.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--active'])[1]").click()
        
        time.sleep(2)
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        docfile = ""
        file_input.send_keys(docfile)
        
        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]").send_keys("Comment")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        
        
        
        
        
        
        
    def searchEmployee(self):
        self.driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys("Comment") # Employee Name
        
        # Specify search
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("") # Employee ID
        
        try: # Employee Status
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        try: # Employee Status
            dropdown = self.driver.find_elements(By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        self.driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("") # Supervisor Name

        self.driver.find_element(By.XPATH, "").send_keys("")
        self.driver.find_element(By.XPATH, "").send_keys("")
        self.driver.find_element(By.XPATH, "").send_keys("")


