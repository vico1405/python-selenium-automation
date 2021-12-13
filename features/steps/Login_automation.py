from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.chrome(executable_path="./chromedriver.exe")
driver.maximize_window()

# open the url
driver.get('//https://www.amazon.com/ap/signin')

# By XPATH
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# By XPATH, two attributes
driver.find_element(By.XPATH,"//input[@id='continue']//a[@class='a-button-input']")
driver.find_element.send_keys('Continue')

# XPATH , Need Help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")


