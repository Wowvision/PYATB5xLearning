from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

@allure.title("VWO Negative Testcase")
@allure.description("TC1 - Negative TC- VWO login with invalid credentials")
@pytest.mark.negativeVWOLogin

def test_app_vwo_login():
    load_dotenv()
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_option)
    driver.get(os.getenv("URL"))


    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element = driver.find_element(By.ID,"login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_web_element = driver.find_element(By.ID,"js-login-btn")
    submit_btn_web_element.click()
    time.sleep(3)

    error_messeage_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_messeage_web_element.text)

    assert error_messeage_web_element.text == os.getenv("error_message_expected")
    driver.quit()


