# pages/user_account_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    PROFILE_URL = "https://vsmonitor.com/user/profile"
    USER_PROFILE_LOCATOR = (By.XPATH, "//body/div[@id='__nuxt']/div[@id='__layout']/div[@class='font-sans flex screen:h-dvh antialiased px-0-safe pb-0-safe']/div[@class='flex flex-col lg:flex-row screen:h-dvh flex-grow w-full pt-safe']/div[@class='bg-white print:hidden bg-primary-800']/div[@id='nav-desktop']/div[@class='flex w-full px-4 mb-2 pt-4 pb-safe']/div[@class='relative _tid_user-menu w-full']/div[@aria-label='nav-user-button']/div[1]")
    MY_USER_ACCOUNT_LOCATOR = (By.XPATH, "//span[@title='My user account']")
    FIRST_NAME_LOCATOR = (By.ID, "firstName")
    LAST_NAME_LOCATOR = (By.ID, "lastName")
    EMAIL_LOCATOR = (By.ID, "email")

    def navigate_to_user_account(self):
        self.click_element(*self.USER_PROFILE_LOCATOR)
        self.click_element(*self.MY_USER_ACCOUNT_LOCATOR)

    def is_on_profile_page(self):
        self.wait_for_url(self.PROFILE_URL)
        return self.get_url() == self.PROFILE_URL

    def get_firstname(self):
        return self.get_disabled_input_value(*self.FIRST_NAME_LOCATOR)

    def get_lastname(self):
        return self.get_disabled_input_value(*self.LAST_NAME_LOCATOR)

    def get_email(self):
        return self.get_disabled_input_value(*self.EMAIL_LOCATOR)