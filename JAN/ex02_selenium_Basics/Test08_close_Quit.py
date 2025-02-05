from selenium import webdriver

import allure
import pytest
import  time

@allure.title("Verify that the title of vwo.vcom as expected")
@pytest.mark.smoke

def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    #driver.close()  #current window close
    driver.quit()  #close everything