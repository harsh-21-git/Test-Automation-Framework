import pytest
from selenium import webdriver

def test_title():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
