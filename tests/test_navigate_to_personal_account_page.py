from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_PAGE_URL, LOGIN_PAGE_URL

# Тест проверки перехода по клику на «Личный кабинет»
def test_navigate_to_personal_account_page(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(LOGIN_PAGE_URL))

    assert driver.current_url == LOGIN_PAGE_URL