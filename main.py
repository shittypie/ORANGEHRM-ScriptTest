from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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

# time.sleep(5)
# cm = clickmodule(driver)
# cm.click_admin()

mt = moduleTabs(driver)
mt.admin()
mt.pim()

# time.sleep(5)
# fc = func(driver)
# fc.addEmployee()



# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]'))
# )
# print("table found")
time.sleep(5)
driver.find_element(By.XPATH, "(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]").click() # Click the first item in the table
print("item selected")

time.sleep(5)

# fc.add_personalDetails()
# time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').click() # Go to contact details
# fc.add_contactDetails()