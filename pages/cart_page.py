from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    PRODUCT_NAME = (By.ID, "//*[@id='productTitle']")

    def open_cart_page(self):
        self.open_page('gp/cart/view.html?ref_=nav_cart')


    def verify_product_name(self, expected_name):
        actual_name = self.driver.find_element(self.PRODUCT_NAME).text
        assert expected_name[:30] in actual_name, f'Expected {expected_name} but got {actual_name}'