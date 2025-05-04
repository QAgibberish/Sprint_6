import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Кликнуть на вопрос")
    def click_on_question(self, number):
        question = MainPageLocators.question(number)
        self.scroll_to_element(question)
        self.click_on_element(question)

    @allure.step("Сравнить ответ")
    def check_answer(self, number, expected_answer):
        actual_answer = self.get_text_on_element(MainPageLocators.answer(number))
        return  actual_answer == expected_answer