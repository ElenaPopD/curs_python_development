import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_iphone_15():
    browser = webdriver.Chrome()
    browser.get("https://www.emag.ro")
    casuta_cautare = browser.find_element(By.NAME, "query")
    casuta_cautare.send_keys("iphone 15")
    casuta_cautare.send_keys(Keys.RETURN)
    iphones = browser.find_elements(By.CLASS_NAME, "card-v2-info")
    assert len(iphones) > 0
