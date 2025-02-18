import time
from dotenv import load_dotenv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import allure
import pytest

@allure.title("Demo ESPOCRM- positiveTC")
@allure.description("TC1-Verify the title of espocrm and current URL ")
@pytest.mark.positive
def test_verify_title_espocrm():
    load_dotenv()
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get(os.getenv("URL_DEMO_ESPCRM"))
    print(driver.title)
    assert driver.title == "EspoCRM Demo"
    print(driver.current_url)
    assert driver.current_url ==os.getenv("URL_DEMO_ESPCRM")
    driver.quit()


@allure.title("Demo ESPOCRM- positiveTC ")
@allure.description("TC2-Click on login button and verify the current URL")
@pytest.mark.positiveTestcase
def test_verify_login_espo_crm():
    load_dotenv()
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get(os.getenv("URL_DEMO_ESPCRM"))
    time.sleep(5)
    login_espo_crm_web_element = driver.find_element(By.ID,"btn-login")
    login_espo_crm_web_element.click()
    time.sleep(5)
    print(driver.current_url)
    assert driver.current_url == os.getenv("URL_DEMO_ESPCRM_LOGIN")
    driver.quit()

@allure.title("Demo ESPOCRM- positiveTC ")
@allure.description("TC3-Click on link text and verify the current URL")
@pytest.mark.positiveTestcase
def test_verify_advanced_pack_link_text_crm():
    load_dotenv()
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get(os.getenv("URL_DEMO_ESPCRM"))
    time.sleep(5)
    advanced_pack_link_text_crm_web_element = driver.find_element(By.LINK_TEXT,"Advanced Pack")
    advanced_pack_link_text_crm_web_element.click()
    time.sleep(5)
    print(driver.current_url)
    assert driver.current_url == os.getenv("URL_DEMO_ESPCRM")
    driver.quit()
