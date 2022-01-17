from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on first product')
def click_first_product(context):
    context.app.search_result_page.click_first_product()

@then('Search result have {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)



'''@then('Search results have table')
def verify_search_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_result = '"table"'

    assert actual_result == expected_result, f'error, actual {actual_result} did not match {expected_result}'''

