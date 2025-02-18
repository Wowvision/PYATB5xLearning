from selenium import webdriver

import allure
import pytest

@allure.title("Verify that the title of vwo.vcom as expected")
@pytest.mark.smoke
def test_Selenium_basic_Commands():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)
    assert driver.title == "Login - VWO"
    print("Current URL is:",driver.current_url)
    print(driver.page_source)
