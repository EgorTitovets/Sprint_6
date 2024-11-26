import allure
import pytest
from Sprint_6.data import QUESTIONS_AND_ANSWERS
from Sprint_6.pages.main_page import MainPage


@allure.suite('Тесты главной страницы')
class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description(
        'Тест проверяет, что текст ответа в разделе "Вопросы о важном", соответствует ожидаемому результату при '
        'выборе определённого вопроса.')
    @pytest.mark.parametrize('num, result', QUESTIONS_AND_ANSWERS)
    def test_questions_and_answers(self, driver, accept_cookies, num, result):
        main_page = MainPage(driver)
        assert main_page.check_question_and_answer(num) == result
