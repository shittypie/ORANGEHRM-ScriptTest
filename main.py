from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Library.take_ss import take_screenshot
from modules import *

import time



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

time.sleep(10)
lm = loginpage_modules(driver)
lm.login(username="Admin", password="admin123")
# screenshot_path = take_screenshot(driver , folder_path = "ORANGEHRM-ScriptTest\Screenshots", file_name="001 Login.png")
# driver.find_element(By.CLASS_NAME, "oxd-button--main").click()

time.sleep(5)
cm = clickmodule(driver)
cm.click_pim()

# time.sleep(5)
# fc = func(driver)
# fc.addEmployee()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]'))
)
print("table found")
first_row = driver.find_element(By.XPATH, "(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]")
first_row.click()

time.sleep(10)
firstname = driver.find_element(By.NAME, "firstName")
firstname.send_keys(Keys.CONTROL + "a") 
firstname.send_keys(Keys.BACKSPACE)
firstname.send_keys("first")
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
# time.sleep(5)

# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("23453")
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys("23453") # Other ID (Optional)

# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("23453") # Driver's license no (Optional)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("2025-12-12") # license Expiry Date
time.sleep(10)

# dropdown_element = driver.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']//div[@class='oxd-select-text-input']")

#--------------------------------------------------------------------------------------------------

try:
    dropdown = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
    dropdown[0].click()
    options_xpath = "//div[@role='option']"
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, options_xpath))
    )
    next(option for option in options if option.text.strip() == "Australian").click()
    
except Exception as e:
    print(f"An error occurred: {e}")
    
time.sleep(5)

try:
    dropdown = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
    dropdown[1].click()
    options_xpath = "//div[@role='option']"
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, options_xpath))
    )
    next(option for option in options if option.text.strip() == "Single").click()
    
except Exception as e:
    print(f"An error occurred: {e}")

#--------------------------------------------------------------------------------------------------
# dropdown_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']//div[@class='oxd-select-text-input'][1]"))
# )
# print("select dropdown working")
# dropdown_element[2].click()
# print("selected an item")

# dropdown_element = driver.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']//div[@class='oxd-select-text-input']")
# dropdown_element.click()
# print("select dropdown working")
# option_to_select = driver.find_element(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']//div[@class='oxd-select-text-input'][contains(text(), 'Angolan')]")
# option_to_select.click()
# print("selected an item")

# dropdown_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]') # Nationality
# select = Select(dropdown_element)
# select.select_by_visible_text("American")

time.sleep(15)

# time.sleep(2)
# dropdown_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]') # Nationality
# select = Select(dropdown_element)
# select.select_by_visible_text("Single")

# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("2000-12-12") # Date of Birth
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click() # Gender(Male)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label').click() # Gender(Female)

# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click() # Save button 1
# time.sleep(5)
