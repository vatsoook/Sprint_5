from locators import Locators
from url import SIGN_UP_PAGE_URL

# Тест проверки успешной регистрации
def test_registration_success_with_valid_data(driver):
    driver.get(SIGN_UP_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT).send_keys("Ринат")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("ahmetdianovvvv@mail.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Rodos3")
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    success_message = driver.find_element(*Locators.SUCCESS_MESSAGE).text

    assert "Зарегистрироваться" in success_message

# Тест для проверки ошибки для некорректного пароля
def test_registration_fails_with_invalid_password(driver):
    driver.get(SIGN_UP_PAGE_URL)
    driver.find_element(*Locators.NAME_INPUT).send_keys("Ринат")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("ahmetdianovvvv@mail.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("561")
    driver.find_element(*Locators.SUBMIT_BUTTON).click()
    error_message = driver.find_element(*Locators.PASSWORD_ERROR).text

    assert "Некорректный пароль" in error_message