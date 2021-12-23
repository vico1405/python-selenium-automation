from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')
time.sleep(3)

search = driver.find_element(By.ID, 'helpsearch')
search.send_keys('cancel_order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()


