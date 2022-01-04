from selenium import webdrive
from selenium.webdriver.common.by import By


driver = webdriver.chrome('C:\\Users\\victo\\OneDrive\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe')

# using css selector for an element with ID by ID
driver.find_elements(By.CSS_SELECTOR, "input#twotabsearchtextbox")
driver.find_elements(By.CSS_SELECTOR, "#twotabsearchtextbox")

# using classes
# 1 class:
driver.find_elements(By.CSS_SELECTOR,"span.a-color-state")
driver.find_elements(By.CSS_SELECTOR,".a-color-sate")

# 2 and more
driver.find_elements(By.CSS_SELECTOR,"span.a-color-state.a-text-bold")
driver.find_elements(By.CSS_SELECTOR,".a-color-state.a-text-bold")

#using attributes
driver.find_elements(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# partial-attr:
driver.find_elements(By.CSS_SELECTOR, "a[href*='ap_signin_notification_condition_of_use']")

# Go from parent to children nodes
driver.find_elements(By.CSS_SELECTOR, "div#legalTextRow a[href*='ap_signin_notification_privacy_notice']")

#class + attributes
driver.find_elements(By.CSS_SELECTOR, "a.nav-a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b'][data-csa-c-type='link']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href*='nav_cs_bestsellers'][data-csa-c-type='link']")