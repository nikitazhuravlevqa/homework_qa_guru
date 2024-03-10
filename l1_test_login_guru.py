from selene import browser, have, be #из селена импортим

# browser.config.browser_name = "firefox" #здесь можно писать любой браузер (стандарт хром)
browser.config.hold_browser_open = True #чтобы браузер оставался открытым
browser.config.timeout = 8.0
def test_can_login(): #запуск теста в pytest
    browser.open("https://school.qa.guru/cms/system/login?required=true")
    browser.element('div.login-form input[name=email]').type("qagurubot@gmail.com") #ищем элемент и вставляем мыло
    browser.element("input[name=password]").type("somepasshere").press_enter()
    browser.element('div.logined-form').should(have.text("QA_GURU_BOT")) #элемент имеет наш текст