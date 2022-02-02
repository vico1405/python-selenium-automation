from bestsellers_page import Bestsellers
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
# from pages.product_page import ProductPage
from pages.search_result_page import SearchResult


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = Bestsellers(self.driver)
        self.cart_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResult(self.driver)

