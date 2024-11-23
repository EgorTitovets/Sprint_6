import allure
import pytest
from Sprint_6.pages.switch_page import SwitchPage
from Sprint_6.pages.main_page import BasePage
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.locators.switch_page_locators import SwitchPageLocators
from Sprint_6.locators.order_page_locators import OrderPageLocators


@allure.title('Тесты переходов между страницами')
class TestSwitchPage:

    @allure.title('Проверка редиректа на главную страницу Дзена по логотипу Яндекса')
    @allure.description(
        'Тест проверяет, что при нажатии на логотип Яндекса, открывается новое окно '
        'с главной страницей Дзена через редирект.'
    )
    def test_yandex_logo_redirect_to_dzen(self, driver, locator=SwitchPageLocators.YANDEX_DZEN_ICON,
                                          expected_text='Поиск Яндекса'):
        base_page = BasePage(driver)
        with allure.step("Нажимаем на логотип Яндекса"):
            base_page.click_to_element(MainPageLocators.YANDEX_LOGO)
        switch_page = SwitchPage(driver)
        with allure.step("Переходим на открывшуюся новую страницу и вкладку"):
            switch_page.switch_to_new_window(locator, expected_text)
        with allure.step(
                "Проверяем, что открылась главная страница Дзена, и на ней виден элемент с текстом 'Поиск Яндекса'"):
            assert base_page.get_text_from_element(SwitchPageLocators.YANDEX_DZEN_ICON) == 'Поиск Яндекса'

    @allure.title("Проверка редиректа на главную страницу 'Самоката' по клику на логотип")
    @allure.description(
        "Тест проверяет, что при нажатии на логотип 'Самоката' открывается главная страница 'Самоката'."
    )
    def test_scooter_logo_redirect_to_main_page(self, driver):
        base_page = BasePage(driver)
        with allure.step("Нажимаем на кнопку Заказать на главной странице"):
            base_page.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)
        with allure.step("Начинаем заполнять форму Заказа, заполняем поле Имя"):
            base_page.add_text_to_element(OrderPageLocators.NAME_INPUT, "Иван")
        with allure.step("Нажимаем на логотип Самоката"):
            base_page.click_to_element(MainPageLocators.SCOOTER_LOGO)
        with allure.step(
                "Проверяем, что открылась главная страница Самоката, и на ней есть текст/описание 'Привезём его прямо к вашей двери'"):
            element = base_page.find_element_with_wait(MainPageLocators.UNIQUE_DESCRIPTION)
            assert element.is_displayed(), 'Привезём его прямо к вашей двери'