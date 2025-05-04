import allure
import pytest
from Data import data
from pages.main_page import MainPage


class TestAnswerText:
    @allure.title("Тест ответов на вопросы")
    @pytest.mark.parametrize('number, expected_answer', data.Data.answers)
    def test_answer_text(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.click_on_question(number)
        assert main_page.check_answer(number, expected_answer)