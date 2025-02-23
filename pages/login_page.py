from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    SSO_LOGIN_BUTTON = (By.XPATH, "//button[@aria-label='btn-sso']")

    def login(self, email, password):
        self.enter_text(*self.EMAIL_INPUT, email)
        self.enter_text(*self.PASSWORD_INPUT, password)
        self.click_element(*self.LOGIN_BUTTON)

    def click_sso_login(self):
        self.click_element(*self.SSO_LOGIN_BUTTON)
