from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on first product')
def click_first_product(context):
    context.app.search_result_page.click_first_product()



@then('Search result have {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@then('Verify baby department is selected')
def verify_department(context):
    context.app.search_result_page.verify_correct_department()


@step("Input car seat into amazon search")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Input car seat into amazon search')