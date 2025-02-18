from selenium import webdriver

import allure
import pytest

def test_sample_vwo_Selenium3():

    driver_path = 'C:/Users/varti/ownloads/edgedriver_win64'
    driver = webdriver.EdgeService(executable_path=driver_path)
    driver.get("https://app.vwo.com")
