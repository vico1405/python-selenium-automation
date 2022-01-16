from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


link = (By.CSS_SELECTOR, "#nav-xshop > a:nth-child(2)")
link_options = (By.XPATH, '//a[contains(@href, "ref=zg_bs_tab")]')

@when('Click on bestseller link on top menu')
def click_bestseller_link(context):
    sleep(5)
    context.driver.find_element(*link).click()

@when('Click on each top link')
def click_top_link(context):
    context.driver.find_element(*link_options).click()

@then('Verify correct page opens')
def verify_correct_page(context):
    expected_link = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']

    for i in range(len(expected_link)):
        link = context.driver.find_elements(*link_options)[i]
        link.click()
        actual_link = link.text
        assert actual_link == expected_link[i], f'Expected {expected_link[i]}, but got {actual_link}'