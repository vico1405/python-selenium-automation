from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon Product B07BJKRR25 page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = [
        'Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed','Dark Wash','Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage',
        'Medium Wash','Rinsed','Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive','Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        assert actual_color == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'


# @when('Click on Add to cart button')
# def click_add_to_cart(context):
 #   context.driver.find_element(*ADD_TO_CART_BTN).click()
  #  sleep(1)




#   assert actual_colors == expected_colors[i], f'Expected {expected_colors[i]}, but got {actual_color}'