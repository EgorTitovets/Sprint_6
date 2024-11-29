import allure

from Sprint_6.locators.switch_page_locators import SwitchPageLocators
from Sprint_6.pages.base_page import BasePage

class SwitchPage(BasePage):
    @allure.step ("Переходим на новую страницу/вкладку и проверяем корректность страницы ")
    def verify_redirect_to_dzen(self):
        self.switch_to_last_window()
        dzen_icon = self.find_element_with_wait(SwitchPageLocators.YANDEX_DZEN_ICON)
        assert dzen_icon.text == 'Поиск Яндекса', "Текст на странице не совпадает с ожидаемым"

