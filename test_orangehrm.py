import pytest
import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    yield driver
    driver.quit()

def wait_for(driver, by, identifier, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, identifier)))

def test_valid_login(driver):
    wait_for(driver, By.NAME, "username").send_keys("Admin")
    wait_for(driver, By.NAME, "password").send_keys("admin123")
    wait_for(driver, By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "/dashboard" in driver.current_url
def test_fail_login(driver):
    wait_for(driver, By.NAME, "username").send_keys("Admin")
    wait_for(driver, By.NAME, "password").send_keys("admin123")
    wait_for(driver, By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    assert "/dashboard/fail" in driver.current_url

def test_invalid_login(driver):
    wait_for(driver, By.NAME, "username").send_keys("invalid")
    wait_for(driver, By.NAME, "password").send_keys("wrongpass")
    wait_for(driver, By.CSS_SELECTOR, "button[type='submit']").click()
    error_msg = wait_for(driver, By.CLASS_NAME, "oxd-alert-content-text").text
    assert "Invalid credentials" in error_msg


@pytest.mark.skipif(sys.platform == "win32", reason="Windows ortamında bu test çalıştırılmaz")
def test_only_on_linux():
    assert True

def test_empty_fields(driver):
    wait_for(driver, By.CSS_SELECTOR, "button[type='submit']").click()
    errors = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-input-field-error-message"))
    )
    assert len(errors)
def test_admin_page_navigation(driver):
    # Login
    wait_for(driver, By.NAME, "username").send_keys("Admin")
    wait_for(driver, By.NAME, "password").send_keys("admin123")
    wait_for(driver, By.CSS_SELECTOR, "button[type='submit']").click()

    # Menüde "Admin" bağlantısını bulup tıkla
    admin_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
    )
    admin_tab.click()

    # Sayfanın yüklenmesini bekle ve URL kontrolü yap
    WebDriverWait(driver, 10).until(EC.url_contains("admin/viewSystemUsers"))
    assert "admin/viewSystemUsers" in driver.current_url
