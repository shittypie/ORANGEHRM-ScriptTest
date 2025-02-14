from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


opt=Options() 
opt.add_experimental_option("debuggerAddress", "localhost:8989") 
ChromeDriverPath = ""
service = Service(ChromeDriverPath)
driver = webdriver.Chrome(service=service, options=opt)  
# driver = webdriver.Chrome(executable_path="C:\\Users\\Mark Roel Andaya\\Documents\\ORANGEHRM-ScriptTest\\Assets\\Chromedriver.exe", chrome_options=opt) 
driver.get("https://www.facebook.com")
driver.find_element(By.ID, "email").send_keys("mark")

# Reference: https://www.youtube.com/watch?v=Zrx8FSEo9lk