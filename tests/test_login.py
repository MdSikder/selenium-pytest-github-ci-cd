import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login import LoginPage  # Assuming the LoginPage is in login_page.py
from utils.logger import logger  # Importing the logger utility
from config import Config


def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    try:
        # Initialize the LoginPage object
        login_page = LoginPage(driver)

        # Open the page and perform actions
        # driver.get("https://rahulshettyacademy.com/loginpagePractise/")

        base_url = Config.BASE_URL
        driver.get(base_url)
        logger.info(f"{base_url} url opened successfully")
        print(f"{base_url} url opened successfully")

        login_page.login(Config.USERNAME, Config.PASSWORD)
        # login_page.login("rahulshettyacademy", "learning")
        logger.info("username and password set successfully")

        # Check if login was successful
        time.sleep(5)  # Wait for login to complete
        assert "ProtoCommerce" in driver.title
    finally:
        driver.quit()

