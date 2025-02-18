from selenium import webdriver

import allure
import pytest

@allure.title("Verify the espocrm title and Current URL")
@pytest.mark.smoke
def test_title_current_url():
    driver = webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    print(driver.title)
    assert driver.title == "EspoCRM Demo"
    print(driver.current_url)
    assert driver.current_url == "https://demo.us.espocrm.com/"