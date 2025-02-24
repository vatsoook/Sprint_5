from locators import Locators
from url import MAIN_PAGE_URL, REGISTER_PAGE_URL, FORGOT_PASSWORD_URL
from constants import EMAIL, PASSWORD

# Тест для входа по кнопке «Войти в аккаунт» на главной странице
def test_login_via_main_page_login_button(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку "Личный кабинет"
def test_login_via_personal_account_button(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку в форме регистрации
def test_login_via_registration_login_button(driver):
    driver.get(REGISTER_PAGE_URL)
    driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()

# Тест для входа через кнопку в форме восстановления пароля
def test_login_via_password_recovery_button(driver):
    driver.get(FORGOT_PASSWORD_URL)
    driver.find_element(*Locators.LOGIN_BUTTON_RECOVERY).click()
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    assert driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).is_displayed()