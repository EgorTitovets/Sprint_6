from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class = 'Button_Button__ra12g' and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']")
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, "//div[@id='accordion__heading-7']")

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    UNIQUE_DESCRIPTION = (By.XPATH, "//div[contains(text(), 'Привезём его прямо к вашей двери')]")

    CONFIRM_COOKIES_BUTTON = (By.ID, "rcc-confirm-button")

