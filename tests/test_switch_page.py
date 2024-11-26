import allure
from Sprint_6.pages.switch_page import SwitchPage
from Sprint_6.pages.main_page import MainPage


@allure.suite('Тесты переходов между страницами')
class TestSwitchPage:

    @allure.title('Проверка редиректа на главную страницу Дзена по логотипу Яндекса')
    @allure.description(
        'Тест проверяет, что при нажатии на логотип Яндекса, открывается новое окно '
        'с главной страницей Дзена через редирект.'
    )
    def test_yandex_logo_redirect_to_dzen(self, driver, accept_cookies):
        main_page = MainPage(driver)
        switch_page = SwitchPage(driver)
        main_page.click_yandex_logo()
        switch_page.verify_redirect_to_dzen()

    @allure.title("Проверка редиректа на главную страницу 'Самоката' по клику на логотип")
    @allure.description(
        "Тест проверяет, что при нажатии на логотип 'Самоката' открывается главная страница 'Самоката'."
    )
    def test_scooter_logo_redirect_to_main_page(self, driver, accept_cookies):
        main_page = MainPage(driver)
        main_page.click_to_order_button_top()
        main_page.click_scooter_logo()
        assert main_page.is_unique_description_displayed(), "Привезём его прямо к вашей двери"
