#There are three types of alert in selenium where you have
#to handle
# 1. Simple javascript alert
#2. Confirm alert with two buttons
#3. Prompt alert where you type any input to confirm the task
#exp:- For provide username and password to access the URL
#2. In travelling side without enter source and destination you have not allowed
# to go ahed

import time
import allure
import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("alert")
@allure.description("verify the alerts")

def test_alerts_js_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_alert = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    js_alert.click()

    WebDriverWait(driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    alert_result = driver.find_element(By.ID,"result")
    alert_result.text
    assert alert_result.text == "You successfully clicked an alert"

    time.sleep(5)





def test_alert_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()



def test_alert_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_confirm.click()

    WebDriverWait(driver, timeout=3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Shubham")
    alert.accept()

    alert_result = driver.find_element(By.ID,"result").text
    assert alert_result == "You entered: Shubham"

    time.sleep(5)
