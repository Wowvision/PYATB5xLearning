import time
import allure
import pytest


from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

@allure.title("App.vwo.com Explicit Wait")
@allure.description("Verify that the App.vwo.com is loaded with waits")

def test_negitive_test_App_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5)

    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("passsword@1234")

    login_web_element = driver.find_element(By.ID,"js-login-btn")
    login_web_element.click()

    ignored_list = [ElementNotVisibleException, ElementNotSelectableException]

    WebDriverWait(driver=driver,poll_frequency=1, timeout=5, ignored_exceptions=ignored_list).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))

    error_message_discripton = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_discripton.text)
    assert error_message_discripton.text == "Your email, password, IP address or location did not match"
