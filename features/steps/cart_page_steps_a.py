from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Amazon Orders link')
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-orders span.nav-line-2').click()
#    context.app.header.click_orders_link()



@then('Verify Sign In page is opened')
def sign_in(context):
    assert 'https://www.amazon.com/ap/signin?_encoding' in context.driver.current_url

