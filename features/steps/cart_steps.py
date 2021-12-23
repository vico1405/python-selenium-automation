from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li" )




@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error, {actual_count} did not match  {expected_count}'

@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert "Mens Watches Ultra-Thin Minimalist Waterproof-Fashion Wrist Watch for Men Unisex Dress with Leather Band" in actual_name, f'Expected {context.product_name} {actual_name}'