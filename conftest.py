import pytest
from selenium import webdriver
from Sprint_6.data import Urls
from Sprint_6.pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_page_url)
    yield driver
    driver.quit()

@pytest.fixture
def accept_cookies(driver):
    main_page = MainPage(driver)
    main_page.accept_cookies()



