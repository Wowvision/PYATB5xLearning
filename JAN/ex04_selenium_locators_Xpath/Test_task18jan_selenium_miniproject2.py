from selenium import webdriver

import allure
import pytest
import time
from selenium.webdriver.common.by import By


@allure.title("Verify the registration page on awesomeQA")
@allure.description("TC - verify the registration page")
@pytest.mark.positive

def test_registration_page_awesomeQA():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_web_element = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name_web_element.send_keys("shubham")

    last_name_web_element = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name_web_element.send_keys("goel")

    email_web_element = driver.find_element(By.XPATH, "//input[@placeholder='E-Mail']")
    email_web_element.send_keys("s1goel@s1.com")

    phone_number_web_element = driver.find_element(By.XPATH,"//input[@placeholder='Telephone']")
    phone_number_web_element.send_keys("9876543212")

    password_web_element = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    password_web_element.send_keys("newuser")

    confirm_password_web_element = driver.find_element(By.XPATH, "//input[@placeholder='Password Confirm']")
    confirm_password_web_element.send_keys("newuser")

    checkbox_web_element = driver.find_element(By.XPATH,"//input[@type='checkbox']")
    checkbox_web_element.click()

    continue_button_web_element = driver.find_element(By.XPATH,"//input[@type='submit']")
    continue_button_web_element.click()
    time.sleep(5)
    messeage_web_element = driver.find_element(By.XPATH,"//div[@id='content']/child::h1")
    print(messeage_web_element.text)
    assert messeage_web_element.text =="Your Account Has Been Created!"


    driver.quit()


