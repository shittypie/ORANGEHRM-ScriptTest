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
        empId.send_keys("500")
        
        elem = WebDriverWait(self.driver, 5).until( # Enable Create Login Details
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-switch-input.oxd-switch-input--active.--label-right"))
        )
        self.driver.execute_script("arguments[0].click();", elem)
        
        time.sleep(5)
        
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("juan12345")
        
        # Enable or disable to make an account (Optional)
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Enabled']").click()
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Disabled']").click()
        
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("juan12345")
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("juan12345")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click() 
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()

    def add_personalDetails(self): # Personal Details/Personal Details
        
        # Just use this when you are lazy 
        # fields = [
        #     "//input[@placeholder='First Name']",
        #     "//input[@placeholder='Middle Name']",
        #     "//input[@placeholder='Last Name']"
        # ]
        # result = textfield.clear_fields(self.driver, fields)
        
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstName").send_keys("first")
        self.driver.find_element(By.NAME, "middleName").send_keys("mid")
        self.driver.find_element(By.NAME, "lastName").send_keys("last")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("23453") # ID
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("23453") # Other ID (Optional)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("23453") # Driver's license no (Optional)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("2025-12-12") # license Expiry Date
        time.sleep(2)
        try: # Nationality
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Australian").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
        time.sleep(2)
        try: # Marital Status
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[1].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Single").click()
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("2000-12-12")
        
        mGender = "//label[normalize-space()='Male']"
        fGender = "//label[normalize-space()='Female']"
        self.driver.find_element(By.XPATH, mGender).click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click() # Save button 1

    def add_contactDetails(self): # Personal Details/Contacts Details
        # Address Section
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("") # Street 1
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("") # Street 2
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("City") # City
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("") # State/Provice
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[6]").send_keys("1111") # Zip/Postal Code
        
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
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[7]").send_keys("12345678") # Home
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[8]").send_keys("12345678") # Mobile
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[9]").send_keys("12345678") # Work
        
        # Email Section
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[10]").send_keys("sad@das.xyz") # Email
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[11]").send_keys("sad@gmail.com") # Other Email
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click() # Save button
        
    def emergencyContacts(self): # Personal Details/Emergency Contacts
        # Assigned emergency contacts section
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Emergency Contacts'])[1]").click()
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]").click()
        
        self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-chevron-left']").click() # In case na Mabasa yung search bar
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[1]").send_keys("Name")
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Relationship")
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("Home Tel")
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("Mobile")
        self.driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("Work Tel")
        
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
        
    def dependentss(self):
        time.sleep(2)


