from selenium.webdriver.common.by import By
from behave import given, when, then

Mens_watch = (By.CSS_SELECTOR, '#imgTagWrapperId')

# @given('Open Amazon page')
# def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')


@when('Search for table')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

#@when('Click search icon')
#def click_search_icon(context):
 #   context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify watch is in cart')
def verify_watch_in_cart_present(context):
    context.driver.find_element()


@then("Amazon cart is empty")
def amazon_cart_is_empty(context):
    context.driver.find_element()
#       raise NotImplementedError(u'STEP: Then Amazon cart is empty')