from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

Mens_watch = (By.CSS_SELECTOR, '#imgTagWrapperId')
DEPARTMENT_DROPDOWN = (By.CSS_SELECTOR, '#searchDropdownBox')
SIGN_IN_BTN = (By.ID, 'nav-link-accountList-nav-line-1')

@given('Open product page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')
#    context.app.main_page.open()


@when('Search for keyword')
def search_amazon(context):
#    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('keyword')
    context.app.header.search_input('keyword')




#@when('Click search icon')
#def click_search_icon(context):
 #   context.driver.find_element(By.ID, 'nav-search-submit-button').click()
#    context.app.header.click_search()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@when('Click sign in from popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN))
    e.click()

@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))

@when('Hover new arrival')
def hover_new(context):
    context.app.main_page.hover_new()

@when('Select department by alias baby')
def select_baby_department(context):
    context.app.header.select_department()

@when('Input {text} into amazon search')
def verify_input_car_seat(context, text):
    context.app.header.enter_text(text)


@then('Sign in pop up is visible')
def verify_signin_popup_visible(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN),)

@then('Verify watch is in cart')
def verify_watch_in_cart_present(context):
    context.driver.find_element()


@then("Amazon cart is empty")
def amazon_cart_is_empty(context):
    context.driver.find_element()


@then('Verify users see deal')
def verify_users_deal(context):
    context.app.main_page.verify_deal()

