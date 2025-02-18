from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Verify free trial")
@allure.description("TC2 - Verify free trial link")
@pytest.mark.freetrial

def test_app_vwo_free_trial():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button_web_element = driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    make_appointment_button_web_element.click()
    time.sleep(5)
    driver.quit()


