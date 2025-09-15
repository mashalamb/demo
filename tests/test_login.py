from pages.login_page import loginForm

def test_login(driver):
    lg = loginForm(driver)
    lg.load("https://practicetestautomation.com/practice-test-login/")
    lg.fillForm("student","Password123")

    assert "logged-in-successfully" in driver.current_url
