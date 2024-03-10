import pytest
from selene import browser, have
@pytest.fixture
def browser_settings():
    browser.config.window_width = 1000
    browser.config.window_height = 1000

def test_google_positive(browser_settings):
    browser.open("https://www.google.com/")
    browser.element("#APjFqb").type("yashaka/selene").press_enter()
    browser.element("[id=search]").should(have.text("yashaka/selene: User-oriented Web UI browser"))

def test_google_negative(browser_settings):
    browser.open("https://www.google.com/")
    browser.element("#APjFqb").type("1165212496249519751759157").press_enter().press_enter()
    browser.element(".card-section").should(have.text("По запросу 1165212496249519751759157 ничего не найдено. "))