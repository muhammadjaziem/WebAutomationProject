import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.page_load_strategy = 'eager'

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.login_page = LoginPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        save_screenshot(context, scenario.name)

    context.driver.delete_all_cookies()


def after_all(context):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()


def save_screenshot(context, scenario_name):
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    file_name = f"{screenshots_dir}/{scenario_name.replace(' ', '_')}.png"
    context.driver.save_screenshot(file_name)
