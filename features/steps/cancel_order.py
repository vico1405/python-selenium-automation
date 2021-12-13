from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import keys

driver = webdriver.chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')
time.sleep(3)

search = driver.find_elements(By.ID, 'helpsearch')
search.send_keys('cancel_order', keys.ENTER)

actual_text = driver.find_elements(By.XPATH, "//div@class='help-content/h1']").text
expected_text = 'Cancel items or orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()


