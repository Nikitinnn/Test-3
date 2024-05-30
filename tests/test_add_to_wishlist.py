from conftest import BaseTest
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.usefixtures("driver_init")
class TestAddToWishlist(BaseTest):

    def test_add_to_wishlist(self):
        self.driver.get("https://dns-shop.ru/") 
        main_page = MainPage(self.driver)
        product_page = ProductPage(self.driver)

        main_page.navigate_to_product()
        product_page.add_to_wishlist()

        assert product_page.is_product_in_wishlist("DEXP")  
