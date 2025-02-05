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

    all_links_page = driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links_page))
    for i in all_links_page:
        print(i.text)
        if "Start a free trial" in i.text:
         i.click()
    driver.quit()


