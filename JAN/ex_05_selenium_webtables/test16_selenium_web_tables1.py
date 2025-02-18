from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import allure

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    #driver.maximize_window()

    #we need to find how many coloumns and rows in table

    row_elements =  driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements =  driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")

    col = len(col_elements)
    print(col)

    #generate dynamic x path
    first_step = "//table[@id='customers']/tbody/tr["
    second_step = "]/td["
    third_step = "]"

    for i in range(2, row+1):
        for j in range(1, col+1):
            dynamic_path = f"{first_step}{i}{second_step}{j}{third_step}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_name = driver.find_element(By.XPATH, country_path).text
                print(f"helen Bennett is in {country_name}")
