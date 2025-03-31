from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



class EmployeeManagement:
    # -------------- Usage -------------- #
    # from TC02_AddEmployee import NewEmployee
    
    # ne = NewEmloyee(l.driver)
    # ne.AddEmployee()
    # -------------- Usage -------------- #
    
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
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Enabled']").click()
        # self.driver.find_element(By.XPATH, "//label[normalize-space()='Disabled']").click()
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[1]").send_keys("juan12345")
        self.driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("juan12345")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click() # Save button
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
        
    def SelectRow(self): # Select first row from the table of PIM 
        first_row = self.driver.find_element(By.XPATH, "(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]")
        # first_row.click()