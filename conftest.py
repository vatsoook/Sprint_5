import pytest
from locators import Locators
from url import LOGIN_PAGE_URL
from selenium import webdriver

@pytest.fixture
def login(driver):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("ahmetdianovvvv@mail.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("Rodos3")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    yield

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()