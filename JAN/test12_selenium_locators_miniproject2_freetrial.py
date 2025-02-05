from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

@allure.title("Verify free trial")
@allure.description("TC2 - Verify free trial link")
@pytest.mark.freetrial

def test_app_vwo_free_trial():
    load_dotenv()
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get(os.getenv("URL"))


    anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element.click()


    assert driver.current_url =="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(3)
    driver.quit()


