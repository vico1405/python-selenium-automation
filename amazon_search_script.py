from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/python-selenium-automation/chromedriver.exe')


driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_result = '"table"'

assert actual_result == expected_result, f'error, actual {actual_result} did not match {expected_result}'

print('Test case passed')
driver.quit()



