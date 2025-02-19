import pytest
from locators import Locators
from url import SIGN_IN_PAGE_URL
from selenium import webdriver

@pytest.fixture
def login(driver):
    driver.get(SIGN_IN_PAGE_URL)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("ahmetdianovvvv@mail.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("Rodos3")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    yield

@pytest.fixture(scope="function")
def driver():
        driver = webdriver.Chrome()  # или другой драйвер
        yield driver
        driver.quit()