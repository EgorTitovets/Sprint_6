from selenium.webdriver.common.by import By

class OrderPageLocators:
    # форма заказа Часть 1
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # ADDRESS_INPUT
    METRO_STATION_INPUT_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_CHERKIZOVSKAYA = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Черкизовская']")
    METRO_STATION_LUBYANKA = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='Лубянка']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    # форма заказа Часть 2
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")
    SELECTED_DELIVERY_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and contains(@class, 'react-datepicker__day--selected')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    RENTAL_PERIOD_FIVE_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']")
    SCOOTER_COLOR_BLACK = (By.XPATH, "//input[@id='black' and @type='checkbox']")
    SCOOTER_COLOR_GREY = (By.XPATH, "//input[@id='grey' and @type='checkbox']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_ORDER_YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

    ORDER_CONFIRMED_MESSAGE = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
