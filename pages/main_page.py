from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


from pages.base_page import Page


class MainPage(Page):
    CART_ICON = (By.ID, 'nav-cart-count-container')
    CART = (By.ID, 'nav-cart-count')
    ARRIVAL = (By.CSS_SELECTOR, 'a[href *= "/New-Arrivals/b/?"]')
    DEALS = (By.XPATH, "//ul[@class='mm-category-list']/li[contains(text(),'See More')]")

#    def open_page(self):
#        self.open_page('https://www.amazon.com/')


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def cart_icon(self):
        self.click(*self.CART_ICON)

    def hover_new(self):
        arrival = self.find_element(*self.ARRIVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(arrival)
        actions.perform()

    def verify_deal(self):
        self.wait_for_element_appear(*self.DEALS)


    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)


