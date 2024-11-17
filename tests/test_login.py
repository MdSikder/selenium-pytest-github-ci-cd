import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login import LoginPage  # Assuming the LoginPage is in login_page.py


def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Initialize the LoginPage object
        login_page = LoginPage(driver)

        # Open the page and perform actions
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        login_page.login("rahulshettyacademy", "learning")

        # Check if login was successful
        time.sleep(5)  # Wait for login to complete
        assert "ProtoCommerce" in driver.title
    finally:
        driver.quit()
