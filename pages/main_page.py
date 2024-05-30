from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def navigate_to_product(self):
        product_locator = (By.CSS_SELECTOR, ".product-link")
        self.click_element(*product_locator)
