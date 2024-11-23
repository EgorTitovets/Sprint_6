
from Sprint_6.locators.order_page_locators import OrderPageLocators
from Sprint_6.pages.base_page import BasePage

class OrderPage(BasePage):

    def set_order_part_1(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, order_data["name"])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, order_data["last_name"])
        self.add_text_to_element(OrderPageLocators.DELIVERY_ADDRESS_INPUT, order_data["address"])
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT_FIELD)
        self.click_to_element(order_data["station_locator"])
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT, order_data["phone_number"])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    def set_order_part_2(self, order_data):
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_INPUT, order_data["delivery_date"])
        self.click_to_element(OrderPageLocators.SELECTED_DELIVERY_DATE)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_to_element(order_data["rental_period"])
        self.click_to_element(order_data["scooter_color"])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_YES_BUTTON)

    def check_order(self, locator):
        return self.get_text_from_element(locator)
