# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_for_title(self, title):
        self.wait.until(EC.title_contains(title))

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def get_disabled_input_value(self, by, value):
        element = self.find_element(by, value)
        return self.driver.execute_script("return arguments[0].value;", element)

