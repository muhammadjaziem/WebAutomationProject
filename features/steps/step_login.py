from behave import given, when, then
from pages.login_page import LoginPage


@given('the user is on the VSM login page')
def step_user_on_login_page(context):
    context.login_page.open_url("https://vsmonitor.com/welcome")


@when('the user clicks the SSO login button')
def step_click_sso_login(context):
    context.login_page.click_sso_login()


@when('the user enters valid credentials')
def step_user_enters_credentials(context):
    email = "muhammadjaziem26@gmail.com"
    password = "TestAccount@123"
    context.login_page.login(email, password)


@then('the user should be redirected to the dashboard page')
def step_verify_dashboard_page(context):
    expected_title = "VistaSoft Monitor"
    context.login_page.wait_for_title(expected_title)
    assert expected_title in context.login_page.get_title(), f"Expected title '{expected_title}', but got '{context.login_page.get_title()}'"


@then('the dashboard URL should be "https://vsmonitor.com/dashboard"')
def step_verify_dashboard_url(context):
    expected_url = "https://vsmonitor.com/dashboard"
    context.login_page.wait_for_url(expected_url)
    assert context.login_page.get_url() == expected_url, f"Expected URL '{expected_url}', but got '{context.login_page.get_url()}'"
