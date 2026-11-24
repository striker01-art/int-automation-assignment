import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()


def test_tc01_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url


def test_tc02_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login_page.get_error_message()


def test_tc03_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "wrong_password_123")
    assert "Username and password do not match any user in this service" in login_page.get_error_message()


def test_tc04_empty_username_validation(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.get_error_message()


def test_tc05_sql_injection_boundary(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("' OR '1'='1", "secret_sauce")
    assert "Username and password do not match any user in this service" in login_page.get_error_message()
