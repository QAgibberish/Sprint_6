from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//span[contains(@class, 'Dropdown-arrow')]")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Да')]")
    STATUS_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Посмотреть статус')]")
    METRO_SELECTOR = (By.CSS_SELECTOR, ".select-search__select")
    ABORT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Отменить заказ')]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    @staticmethod
    def scooter_color(color):
        return By.XPATH, f"//label[contains(@for, '{color}')]"

    @staticmethod
    def metro_string(metro):
        return By.XPATH, f"//div[@class='Order_Text__2broi' and contains(text(), '{metro}')]"

    @staticmethod
    def period_string(period):
        return By.XPATH, f"//div[@class='Dropdown-option' and contains(text(), '{period}')]"