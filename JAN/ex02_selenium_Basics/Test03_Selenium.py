import time

from selenium import webdriver
import allure
import pytest

@allure.title("Open the App.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Chrome()
    #1 This code is translated into API Request
    #2 POST request- browser DRIVER(Server)
    #3 Where it will create a session or Fresh Copy Browser(Chrome)
    #4 Sesion ID -16 digit will be craeted
    driver.get("https://app.vwo.com/#/login")
    #5 Get Request:- Navigate to perticular page
    #6 Browser will navigate to the URL
    driver.maximize_window()
    print(driver.session_id)

