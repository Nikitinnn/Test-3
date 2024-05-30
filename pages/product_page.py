from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_locator = (By.ID, "add-to-cart-button")
        self.click_element(*add_to_cart_locator)

    def add_to_wishlist(self):
        add_to_wishlist_locator = (By.ID, "add-to-wishlist-button")
        self.click_element(*add_to_wishlist_locator)

    def write_review(self, review_text):
        review_input_locator = (By.ID, "review-input")
        submit_review_locator = (By.ID, "submit-review-button")
        self.enter_text(review_text, *review_input_locator)
        self.click_element(*submit_review_locator)
