from selenium.webdriver.common.by import By
from behave import given,when, then

Mens_watch = (By.CSS_SELECTOR, '#imgTagWrapperId')


@when('Search for watch')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('watch')


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify watch is in cart')
def verify_watch_in_cart_present(context):
    context.driver.find_element()

