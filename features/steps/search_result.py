from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li" )
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")



@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Search for Men's watch")
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Men's watch")

@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

@when('Click on Add to cart button')
def click_add_button(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'current product: {context.product_name}')

