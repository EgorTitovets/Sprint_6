import allure

from Sprint_6.locators.order_page_locators import OrderPageLocators
from Sprint_6.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполняем первую часть формы заказа Самоката")
    def set_order_part_1(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, order_data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, order_data["last_name"])
        self.add_text_to_element(OrderPageLocators.DELIVERY_ADDRESS_INPUT, order_data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT_FIELD)
        self.click_to_element(order_data["station_locator"])
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, order_data["phone_number"])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем вторую часть формы заказа Самоката")
    def set_order_part_2(self, order_data):
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_INPUT, order_data["delivery_date"])
        self.click_to_element(OrderPageLocators.SELECTED_DELIVERY_DATE)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_to_element(order_data["rental_period"])
        self.click_to_element(order_data["scooter_color"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_YES_BUTTON)

    @allure.step("Проверяем, что 'Заказ оформлен")
    def is_order_confirmed(self):
        confirmation_message = self.find_element_with_wait(OrderPageLocators.ORDER_CONFIRMED_MESSAGE)
        return "Заказ оформлен" in confirmation_message.text
