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
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='commonModal__close']")))

    modal = driver.find_element(By.XPATH,"//span[@class='commonModal__close']")
    modal.click()



    time.sleep(5)
