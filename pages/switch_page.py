
from Sprint_6.pages.base_page import BasePage

class SwitchPage(BasePage):

    def switch_to_new_window(self, locator, expected_text):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        element = self.find_element_with_wait(locator)
        assert element.text == expected_text


