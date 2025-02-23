import os
from selenium import webdriver
from pages.login_page import LoginPage


def before_all(context):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(20)
    context.driver.maximize_window()


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.login_page = LoginPage(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        save_screenshot(context, scenario.name)

    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.quit()


def save_screenshot(context, scenario_name):
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    file_name = f"{screenshots_dir}/{scenario_name.replace(' ', '_')}.png"
    context.driver.save_screenshot(file_name)
