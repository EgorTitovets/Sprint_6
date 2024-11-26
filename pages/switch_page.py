import allure

from Sprint_6.pages.base_page import BasePage

class SwitchPage(BasePage):
    @allure.step ("Переходим на новую страницу/вкладку и проверяем корректность страницы ")
    def switch_to_new_window(self, locator, expected_text):
        self.switch_to_last_window()
        element = self.find_element_with_wait(locator)
        assert element.text == expected_text




