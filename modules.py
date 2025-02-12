from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

class loginpage_modules:
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        screenshot_path = self.take_screenshot(driver , folder_path = "ORANGEHRM-ScriptTest\Screenshots", file_name="001 Login.png")
        self.driver.find_element(By.CLASS_NAME, "oxd-button--main").click()
        time.sleep(10)   

class clickmodule:
    def __init__(self, driver):
        self.driver = driver
        
    def click_admin(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(5)
        
    def click_pim(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5)
        
    def click_leave(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
        time.sleep(5)
        
    def click_time(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
        time.sleep(5)
        
    def click_recruitment(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
        time.sleep(5)
        
    def click_myInfo(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
        time.sleep(5)
        
    def click_performance(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
        time.sleep(5)