from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import pytest


class Login:
    def __init__(self):
        self.driver = None
    
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Setup initialized...")

    def login(self):
        time.sleep(5)
        username = "Admin"
        password = "admin123"
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Login Successful")

    def close(self):
        time.sleep(2)
        self.driver.quit()
        

        
# if __name__ == "__main__":
#     l = Login() 
#     l.setup()           
#     l.login()           
#     # l.close()   
    
#     time.sleep(3)

@pytest.fixture(scope="module", autouse=True)
def run_login():
    """Automatically executes the test setup, login, and close methods."""
    login_obj = Login()
    login_obj.setup()  # Open browser

    yield login_obj  # Keep browser session open

    login_obj.close()  # Close browser after execution

def test_run(run_login):
    """pytest requires at least one test function to trigger execution."""
    run_login.login()  # Perform login