from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    def register(self, username, password, email):
        username_locator = (By.ID, "username")
        password_locator = (By.ID, "password")
        email_locator = (By.ID, "email")
        register_button_locator = (By.ID, "register-button")
        
        self.enter_text(username, *username_locator)
        self.enter_text(password, *password_locator)
        self.enter_text(email, *email_locator)
        self.click_element(*register_button_locator)
