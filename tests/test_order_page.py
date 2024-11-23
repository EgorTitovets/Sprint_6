import allure
import pytest

import Sprint_6.data
from Sprint_6.pages.main_page import MainPage
from Sprint_6.pages.order_page import OrderPage
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.locators.order_page_locators import OrderPageLocators


@allure.title('Тесты оформления заказа аренды самоката')
class TestOrderPage:

    @allure.title('Проверка флоу заказа для разных точек входа и данных')
    @allure.description(
        'Этот тест проверяет флоу оформления заказа для двух точек входа: '
        'кнопка «Заказать» вверху страницы и внизу, '
        'с использованием двух разных наборов данных.')
    @pytest.mark.parametrize(
        'locator, order_data',
        [
            (MainPageLocators.ORDER_BUTTON_TOP, Sprint_6.data.ORDER_DATA_1),
            (MainPageLocators.ORDER_BUTTON_BOTTOM, Sprint_6.data.ORDER_DATA_2)
        ]
    )
    def test_create_order(self, driver, locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        with allure.step("Нажатие на кнопку 'Заказать'"):
            main_page.click_to_order_button(locator)
        with allure.step("Заполнение первой части формы заказа"):
            order_page.set_order_part_1(order_data)
        with allure.step("Заполнение второй части формы заказа"):
            order_page.set_order_part_2(order_data)
        with allure.step("Проверка, что 'Заказ оформлен'"):
            assert "Заказ оформлен" in order_page.check_order(OrderPageLocators.ORDER_CONFIRMED_MESSAGE)
