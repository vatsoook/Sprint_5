from locators import Locators
from url import MAIN_PAGE_URL

# Тест проверки перехода к разделу "Булки"
def test_navigate_to_buns_section(driver):
    driver.get(MAIN_PAGE_URL)
    driver.find_element(*Locators.BUNS_SECTION_BUTTON).click()
    buns_header = driver.find_element(*Locators.BUNS_SECTION_HEADER)
    assert buns_header.is_displayed(), "Булки"

# Тест проверки перехода к разделу "Соусы"
def test_navigate_to_sauces_section(driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*Locators.SAUCES_SECTION_BUTTON).click()
        buns_header = driver.find_element(*Locators.SAUCES_SECTION_HEADER)
        assert buns_header.is_displayed(), "Соусы"

# Тест проверки перехода к разделу "Начинки"
def test_navigate_to_fillings_section(driver):
            driver.get(MAIN_PAGE_URL)
            driver.find_element(*Locators.FILLINGS_SECTION_BUTTON).click()
            buns_header = driver.find_element(*Locators.FILLINGS_SECTION_HEADER)
            assert buns_header.is_displayed(), "Начинки"