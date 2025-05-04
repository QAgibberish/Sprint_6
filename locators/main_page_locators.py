from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g")
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, ".Home_FinishButton__1_cWm .Button_Button__ra12g")

    @staticmethod
    def question(number):
        return By.ID, f'accordion__heading-{number}'

    @staticmethod
    def answer(number):
        return By.XPATH, f'//*[@id="accordion__panel-{number}"]/p'