from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


link = (By.CSS_SELECTOR, "#nav-xshop > a:nth-child(2)")
link_options = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li')

@when('Click on bestseller link on top menu')
def click_bestseller_link(context):
    sleep(5)
    context.driver.find_element(*link).click()

@when('Click on each top link')
def click_top_link(context):
    context.driver.find_element(*link_options).click()


@then('Verify correct page opens')
def verify_each_element(context):
    TITLES = ['Amazon Best Sellers', 'Amazon Hot New Releases', 'Amazon Movers & Shakers',    'Amazon Most Wished For', 'Amazon Gift Ideas'    ]
    links_len = len(context.driver.find_elements(*link_options))
    print("THE LEN IS", links_len)
    for i in range(links_len):
        context.driver.find_elements(*link_options)[i].click()
        current_title = context.driver.find_element(By.ID, 'zg_banner_text').text
        assert current_title == TITLES[i], f'{current_title} is not {TITLES[i]}'





'''''@then('Verify correct page opens')
def verify_correct_page(context):
    expected_link = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']

    for i in range(len(expected_link)):
        link = context.driver.find_elements(*link_options)[i]
        link.click()
        actual_link = link.text
        assert actual_link == expected_link[i], f'Expected {expected_link[i]}, but got {actual_link}'''