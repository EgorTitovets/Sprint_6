import allure
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверка ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)

    @allure.step('Нажатие на кнопку "Заказать, начало оформления заказа')
    def click_to_order_button(self, locator):
        self.click_to_element(locator)

    @allure.step('Подтверждение cookies на странице')
    def accept_cookies(self):
        self.find_element_with_wait(MainPageLocators.CONFIRM_COOKIES_BUTTON).click()

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Нажатие на кнопку "Заказать, в верхней части страницы')
    def click_to_order_button_top(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажимаем на логотип Самокат')
    def click_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Проверяем отображение уникального описания на главной странице")
    def is_unique_description_displayed(self):
        element = self.find_element_with_wait(MainPageLocators.UNIQUE_DESCRIPTION)
        return element.is_displayed()
