import allure
from Sprint_6.pages.switch_page import SwitchPage
from Sprint_6.pages.main_page import MainPage
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.locators.switch_page_locators import SwitchPageLocators
from Sprint_6.locators.order_page_locators import OrderPageLocators


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
        main_page.click_to_element(MainPageLocators.YANDEX_LOGO)
        switch_page.switch_to_new_window(SwitchPageLocators.YANDEX_DZEN_ICON, 'Поиск Яндекса')
        assert switch_page.get_text_from_element(SwitchPageLocators.YANDEX_DZEN_ICON) == 'Поиск Яндекса'

    @allure.title("Проверка редиректа на главную страницу 'Самоката' по клику на логотип")
    @allure.description(
        "Тест проверяет, что при нажатии на логотип 'Самоката' открывается главная страница 'Самоката'."
    )
    def test_scooter_logo_redirect_to_main_page(self, driver, accept_cookies):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        order_page.add_text_to_element(OrderPageLocators.NAME_INPUT, "Иван")
        main_page.click_to_element(MainPageLocators.SCOOTER_LOGO)
        element = main_page.find_element_with_wait(MainPageLocators.UNIQUE_DESCRIPTION)
        assert element.is_displayed(), 'Привезём его прямо к вашей двери'
