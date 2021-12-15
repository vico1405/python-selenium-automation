from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\victo\\OneDrive\\Desktop\\8-Python-Automation-selenium\\python-selenium-automation\\chromedriver.exe')

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Amazon logo
# using classes
driver.find_elements(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# create account
driver.find_elements(By.CSS_SELECTOR, "h1.a-spacing-small']")
# Input your name
driver.find_elements(By.CSS_ID, "input['#ap_customer_name.a-input-text.a-span12.auth-autofocus.auth-required-field']")

# password
driver.find_elements(By.CSS_ID, "input['#ap_password.a-input-text.a-span12.auth-required-field.auth-require-fields-match.auth-require']")

# password check
driver.find_elements(By.CSS_ID, "input['#ap_password_check.a-input-text.a-span12.auth-required-field.auth-require-fields-match']")

# submit button
driver.find_elements(By.CSS_SELECTOR, "input['#continue.a-button-input']")