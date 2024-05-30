from conftest import BaseTest
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.usefixtures("driver_init")
class TestWriteReview(BaseTest):

    def test_write_review(self):
        self.driver.get("https://dns-shop.ru/")  
        main_page = MainPage(self.driver)
        product_page = ProductPage(self.driver)

        main_page.navigate_to_product()
        product_page.write_review("Это отличный продукт!")

        review_locator = (By.XPATH, "//div[contains(text(), 'Это отличный продукт!')]")
        assert product_page.find_element(*review_locator).is_displayed()
