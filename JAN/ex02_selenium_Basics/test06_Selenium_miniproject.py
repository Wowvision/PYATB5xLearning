from selenium import webdriver

import allure
import pytest

@allure.title("Verify that the title of vwo.vcom as expected")
@pytest.mark.smoke
def test_vwo_sample():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    if "PURA Healthcare Service" in driver.page_source:
        print("Text Found !! test passed")

    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")

#Close the browser? python interpretor close the browser