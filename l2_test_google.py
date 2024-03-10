from selene import browser, have

browser.open("https://www.google.com/")
def test_google():
    browser.element("#APjFqb").type("yashaka/selene").press_enter()
    browser.element("[id=search]").should(have.text("yashaka/selene: User-oriented Web UI browser"))
