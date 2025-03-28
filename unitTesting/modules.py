
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class moduleTabs: # Select all modules from the sidebar menu

    # -------------- Usage -------------- #
    # from unitTesting import modules
    #
    # 
    # get the login function first before calling this function
    #
    # mt = modules.moduleTabs()
    # OR
    # mt = modules.moduleTabs(l.driver) (l = your login func)
    # mt.admin()
    # -------------- Usage -------------- #
    
    def __init__(self, driver):
        self.driver = driver
    
    # def setup(self):
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option("detach", True)
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.maximize_window()
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     print("Setup initialized...")

    # def login(self):
    #     time.sleep(5)
    #     username = "Admin"
    #     password = "admin123"
    #     self.driver.find_element(By.NAME, "username").send_keys(username)
    #     self.driver.find_element(By.NAME, "password").send_keys(password)
    #     self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     print("Login Successful")

        
    def admin(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]").click() 
        time.sleep(2)
        
    def pim(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space(@class='oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'PIM')]").click()
        time.sleep(2)

    def leave(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[normalize-space(@class='oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Leave')]").click()
        time.sleep(2)
        
    def time(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Time')]").click()
        time.sleep(2)

    def recruitment(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Recruitment')]").click()
        time.sleep(2)

    def myInfo(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'My Info')]").click()
        time.sleep(2)

    def performance(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Performance')]").click()
        time.sleep(2)

    def dashboard(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Dashboard')]").click()
        time.sleep(2)

    def directory(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Directory')]").click()
        time.sleep(2)

    def claim(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Claim')]").click()
        time.sleep(2)

    def buzz(self): 
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and contains(., 'Buzz')]").click()
        time.sleep(2)
    

if __name__ == "__main__":
    mt = moduleTabs()
    mt.setup()
    mt.login()
    mt.admin()
    mt.pim()
    mt.leave()
    mt.time()
    mt.recruitment()
    mt.myInfo()
    mt.performance()
    mt.dashboard()
    mt.directory() 
    mt.claim()
    mt.buzz()