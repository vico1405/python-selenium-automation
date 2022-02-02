from selenium.webdriver.common.by import By


from pages.base_page import Page


class SearchResult(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    BABY_SUB_NAV = (By.CSS_SELECTOR, "#nav-subnav span.nav-a-content")

    def input_search(self, car_seat):
        self.wait_for_element_search(*self.BABY_SUB_NAV)


    def click_first_product(self):
        self.wait_for_element_click(*self.PRODUCT_PRICE)


    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, self.SEARCH_RESULT)


    def verify_correct_department(self):
        expected_text = 'Baby'
        self.verify_text(expected_text, *self.BABY_SUB_NAV)