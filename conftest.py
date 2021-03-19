import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("Starting Chrome")
    browser = webdriver.Chrome()
    yield browser
    print("Closing Chrome")
    browser.quit()
