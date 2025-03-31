from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print("Setup initialized...")



time.sleep(5)
username = "Admin"
password = "admin123"
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Login Successful")
time.sleep(5)



class AddEmployeeDetails:
    
    def __init__(self, driver):
        self.driver = None
        
    
    def emergencyContacts(self):
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

        # Attachment
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[2]").click()

        driver.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--focus'])[1]").click()
        time.sleep(2)
        file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')

        docfile = ""
        file_input.send_keys(docfile)

        self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Type comment here'])[1]").send_keys("Comment")

        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[2]").click()
        # driver.find_element(By.XPATH, '(//button[normalize-space()='Cancel'])[2]').click() # Cancel button
