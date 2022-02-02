from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    CART = (By.ID, 'nav-cart-count')
    DEPARTMENT_DROPDOWN = (By.CSS_SELECTOR, '#searchDropdownBox')
    ORDERS_LINK = (By.CSS_SELECTOR, '#nav-orders span.nav-line-2')
    TEXT = (By.XPATH, "//*[@class='a-row sc-your-amazon-cart-is-empty']/h2")
    SEARCH_BAR = (By.ID, 'twotabsearchtextbox')


    def click_order(self):
        self.click(*self.ORDERS_LINK)

    def sign_in_page(self, url):
        self.driver.get('https://www.amazon.com/ap/signin?_encoding')

    def select_department(self):
        dropdown = self.find_element(*self.DEPARTMENT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value('search-alias=baby-products')


    def enter_text(self, text):
        self.input_text(text, *self.SEARCH_BAR)





#    def verify_cart_count(self, expected_count: str):
#        self.verify_text(expected_count, *self.CART)
