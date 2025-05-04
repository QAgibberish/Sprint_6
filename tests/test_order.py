import allure
import pytest
from Data.data import OrderData
from pages.order_page import OrderPage

class TestOrder:
    @allure.title("Тест оформления заказа")
    @pytest.mark.parametrize("order_data,button_position", [
        (OrderData.top_variation, "top"),
        (OrderData.bottom_variation, "bottom")
    ])
    def test_order_scooter(self, driver, order_data, button_position):
        order_page = OrderPage(driver)
        order_page.click_order_button(button_position)
        order_page.input_data(order_data)
        order_page.confirm_order()
        assert order_page.wait_popup()

        order_page.click_to_status_button()
        order_page.click_scooter_logo()
        assert order_page.check_redirect_to_main_page()

        order_page.click_yandex_logo()
        assert order_page.check_redirect_to_dzen()