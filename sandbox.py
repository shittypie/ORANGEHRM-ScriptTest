from selenium.webdriver.common.by import By
import time
from unitTesting import modules
from unitTesting import logIn
from unitTesting.PIMModule import accManagement
from Library.clearFields import textfield

if __name__ == "__main__":
    l = logIn.login()
    l.setup()
    time.sleep(3)
    l.login()
    
    mt = modules.moduleTabs(l.driver)
    retries = 3  
    delay = 2
    for attempt in range(retries):
        try:
            mt.pim()
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                print("All attempts failed.")
    
    am = accManagement.AccountManagement(l.driver)
    am.AddEmployee()
    am.add_personalDetails()
    
    # Tsaka na ito once na mavalidate na lahat ng xpath
    # time.sleep(2)
    # l.driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
    
    # fields = [
    #     "(//input[@class='oxd-input oxd-input--active'])[2]",
    #     "(//input[@class='oxd-input oxd-input--active'])[3]",
    #     "(//input[@class='oxd-input oxd-input--active'])[4]",
    #     "(//input[@class='oxd-input oxd-input--active'])[5]",
    #     "(//input[@class='oxd-input oxd-input--active'])[6]"
    # ]
    # time.sleep(3)
    # textfield.clear_fields(l.driver, fields)
    
    # time.sleep(3)
    # am = accManagement.AccountManagement(l.driver)
    # am.add_personalDetails()