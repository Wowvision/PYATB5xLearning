import time

from selenium import webdriver
import allure
import pytest

@allure.title("Open the App.vwo.com")
@pytest.mark.regression
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(15)