from .base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def is_product_in_cart(self, product_name):
        product_locator = (By.XPATH, f"//div[contains(text(), '{product_name}')]")
        return self.find_element(*product_locator).is_displayed()
