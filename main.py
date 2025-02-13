from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Library.take_ss import take_screenshot
from modules import *

import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

time.sleep(10)
lm = loginpage_modules(driver)
lm.login(username="Admin", password="admin123")
# screenshot_path = take_screenshot(driver , folder_path = "ORANGEHRM-ScriptTest\Screenshots", file_name="001 Login.png")
driver.find_element(By.CLASS_NAME, "oxd-button--main").click()

time.sleep(5)
cm = clickmodule(driver)
cm.click_pim()

time.sleep(5)
fc = func(driver)
fc.addEmployee()
