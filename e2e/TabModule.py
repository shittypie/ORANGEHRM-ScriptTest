from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from TC01_LogIn import Login


class moduleTabs:
    
    # -------------- Usage -------------- #
    # from TC01_LogIn import Login
    # from TabModule import moduleTabs
    
    # l = Login()
    # mt = moduleTabs(l.driver) <-- Driver of Login function
    # mt.admin()
    # -------------- Usage -------------- #
    
    def __init__(self, driver):
        self.driver = driver 
        
    def admin(self):
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Admin"]').click() 
        print("clicked")
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
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # print("Setup initialized...")

    # time.sleep(5)
    # username = "Admin"
    # password = "admin123"
    # driver.find_element(By.NAME, "username").send_keys(username)
    # driver.find_element(By.NAME, "password").send_keys(password)
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # print("Login Successful") 
    
    l = Login() 
    l.setup()           
    l.login()  
    mt = moduleTabs(l.driver)
    time.sleep(5)
    mt.admin()
    
    time.sleep(3)