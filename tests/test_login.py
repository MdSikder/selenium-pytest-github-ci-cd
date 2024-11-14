import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # Locate elements and perform actions
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.XPATH, "//input[@name='signin']").click()

    time.sleep(3)
    # Check if login was successful by checking the page title
    assert "ProtoCommerce" in driver.title

    driver.quit()
