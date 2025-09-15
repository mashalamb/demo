from selenium.webdriver.common.by import By


class loginForm():
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID,"username")
        self.passwd_input = (By.ID,"password")
        self.btn = (By.ID,"submit")

    def load(self,url):
        self.driver.get(url)

    def fillForm(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.passwd_input).send_keys(password)
        self.driver.find_element(*self.btn).click()