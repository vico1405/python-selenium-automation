from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on cart icon')
def click_carts(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()
#    context.app.header.click_carts()


@then("Verify 'Your Shopping Cart is empty' text present")
def verify_text(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_text = 'Your Amazon Cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
#    context.app.cart_page.verify_text(context.current_text)

