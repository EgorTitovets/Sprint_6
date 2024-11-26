import pytest
from selenium import webdriver
from Sprint_6.data import Urls
from Sprint_6.locators.main_page_locators import MainPageLocators


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()

@pytest.fixture
def accept_cookies(driver):
    driver.find_element(*MainPageLocators.CONFIRM_COOKIES_BUTTON).click()

