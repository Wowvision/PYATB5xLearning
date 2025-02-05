from selenium import webdriver

import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_katalon_Chrome():

    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    #chrome_option.add_argument("--start-maximized")
    #chrome_option.add_argument("--window-size=900,600")
    chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    driver.quit()


