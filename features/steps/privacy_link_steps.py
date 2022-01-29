from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


link = (By.XPATH, '//a[contains(@href, "privacy")]')



@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.driver.window_handles)
    print('Original_window:', context.original_window)

@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.driver.find_element(*link).click()

@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
#    context.driver.switch_to_window(windows[1])
    context.driver.switch_to.window(windows[1])

@given("Open Amazon T&C page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@then('Verify Amazon Privacy Notice page is opened')
def switch_to_window(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html' in context.driver.current_url


