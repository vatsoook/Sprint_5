from conftest import login
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import LOGIN_PAGE_URL

# Тест выхода по кнопке «Выйти» в личном кабинете.
def test_logout_functionality(driver, login):
    driver.get(LOGIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.SIGN_OUT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(LOGIN_PAGE_URL))

    assert driver.current_url == LOGIN_PAGE_URL