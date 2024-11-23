import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.get("https://qa-scooter.praktikum-services.ru/")
#     accept_cookies_button = By.ID, "rcc-confirm-button"
#     driver.find_element(*accept_cookies_button).click()
#     yield driver
#     driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    accept_cookies_button = By.ID, "rcc-confirm-button"
    driver.find_element(*accept_cookies_button).click()
    yield driver
    driver.quit()


