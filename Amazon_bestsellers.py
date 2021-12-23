from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="C:\\Users\\victo\\OneDrive\\Desktop\\8-Python-Automation-selenium\\python-selenium-automation\\chromedriver.exe")
driver.maximize_window()

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#zg_header a")

