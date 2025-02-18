from selenium import webdriver

import allure
import pytest
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Verify ebay mac mini titles and prices")
@allure.description("TC1 - Verify ebay title and prices")
@pytest.mark.positive
@allure.step

def test_app_ebay_mac_mini():
    chrome_option = Options()
    chrome_option.add_argument("--incognito")
    chrome_option.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_option)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_content_web_element = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for anything']")
    #search_content_web_element.click()
    search_content_web_element.send_keys("macmini")
    time.sleep(5)
    search_button_click_web_element = driver.find_element(By.XPATH,"//span[text()='Search']")
    search_button_click_web_element.click()

    list_of_items = driver.find_elements(By.XPATH,"//div[@class='s-item__title']")
    list_items_prize = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")
    for item in list_of_items:
     print(item.text)

    print("prize----------------------------------")
    for prize in list_items_prize:
     print(prize.text)

    driver.quit()


