from TC01_LogIn import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time



class moduleTabs:
    
    def __init__(self, driver):
        self.driver = driver
        
    def admin(self):
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Admin"]').click() 
        time.sleep(5)
        
    def pim(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="PIM"]').click()
        time.sleep(2)
        
    def leave(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Leave"]').click()
        time.sleep(2)
    def time(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="time"]').click()
        time.sleep(2)
        
    def recruitment(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Recruitment"]').click()
        time.sleep(2)
        
    def myInfo(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="My Info"]').click()
        time.sleep(2)
        
    def performance(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Performance"]').click()
        time.sleep(2)
        
    def dashboard(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Dashboard"]').click()
        time.sleep(2)
        
    def Directory(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Directory"]').click()
        time.sleep(2)
        
    def claim(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Claim"]').click()
        time.sleep(2)
        
    def buzz(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Buzz"]').click()
        time.sleep(2)
        
    def performance(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Performance"]').click()
        time.sleep(2)




if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    mt = moduleTabs(driver)
    mt.admin()
    mt.pim()
    mt.leave()
    mt.time()
    mt.recruitment()
    mt.myInfo()
    mt.performance()
    mt.dashboard()
    mt.Directory() 
    mt.claim()
    mt.buzz()
    mt.performance()