import allure

from Data.url import *
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators

class OrderPage(BasePage):
    @allure.step("Нажать кнопку «Заказать»")
    def click_order_button(self, button_position='top'):
        if button_position == 'top':
            self.click_on_element(MainPageLocators.TOP_ORDER_BUTTON)
        else:
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
            self.click_on_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Заполнить форму заказа")
    def input_data(self, order_data):
        self.send_keys_to_input(OrderPageLocators.NAME, order_data["name"])
        self.send_keys_to_input(OrderPageLocators.SURNAME, order_data["surname"])
        self.send_keys_to_input(OrderPageLocators.ADDRESS, order_data["address"])
        self.select_metro_station(order_data["metro"])
        self.send_keys_to_input(OrderPageLocators.PHONE, order_data["phone"])
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
        self.send_keys_to_input(OrderPageLocators.DATE, order_data["date"])
        self.select_rental_period(order_data["period"])
        self.click_on_element(OrderPageLocators.scooter_color(order_data["color"]))
        self.send_keys_to_input(OrderPageLocators.COMMENT, order_data["comment"])

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Подождать загрузки всплывающего сообщения")
    def wait_popup(self):
        return self.wait_for_element(OrderPageLocators.STATUS_BUTTON).is_displayed()

    @allure.step("Перейти на страницу статуса заказа")
    def click_to_status_button(self):
        self.click_on_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self, metro):
        self.click_on_element(OrderPageLocators.METRO)
        self.send_keys_to_input(OrderPageLocators.METRO, metro)
        self.click_on_element(OrderPageLocators.metro_string(metro))

    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, period):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.period_string(period))

    @allure.step("Нажать на логотип самоката")
    def click_scooter_logo(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)

    @allure.step("Проверить переход на главную страницу")
    def check_redirect_to_main_page(self):
        actual_url = self.wait_and_get_url(main_site)
        return actual_url == main_site

    @allure.step("Проверить переход на страницу Дзена")
    def check_redirect_to_dzen(self):
        actual_url = self.switch_and_get_url(dzen)
        return actual_url == dzen