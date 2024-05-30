from conftest import BaseTest
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.usefixtures("driver_init")
class TestAddCameraToCart(BaseTest):

    def test_add_camera_to_cart(self):
        self.driver.get("https://dns-shop.ru/")  
        main_page = MainPage(self.driver)
        product_page = ProductPage(self.driver)

        main_page.navigate_to_product()
        product_page.add_to_cart()

        assert product_page.is_product_in_cart("canon 3000")  
