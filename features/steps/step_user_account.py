from behave import given, when, then
from features.steps.step_login import (
    step_user_on_login_page,
    step_click_sso_login,
    step_user_enters_credentials,
    step_verify_dashboard_page,
    step_verify_dashboard_url,
)
from pages.user_account_page import UserAccountPage


@given('I am logged into the application')
def step_impl(context):
    step_user_on_login_page(context)
    step_click_sso_login(context)
    step_user_enters_credentials(context)
    step_verify_dashboard_page(context)
    step_verify_dashboard_url(context)


@when('I navigate to "My user account"')
def step_impl(context):
    user_account_page = UserAccountPage(context.driver)
    user_account_page.navigate_to_user_account()


@then('I should be on the user profile page')
def step_impl(context):
    user_account_page = UserAccountPage(context.driver)
    assert user_account_page.is_on_profile_page(), \
        f"Expected {UserAccountPage.PROFILE_URL}, but got {user_account_page.get_url()}"


@then('my firstname and lastname should be "Test" and "Account"')
def step_impl(context):
    user_account_page = UserAccountPage(context.driver)

    first_name = user_account_page.get_firstname()
    last_name = user_account_page.get_lastname()

    assert first_name == "Test", f"Expected first name 'Test', but got '{first_name}'"
    assert last_name == "Account", f"Expected last name 'Account', but got '{last_name}'"


@then('my email should be "muhammadjaziem26@gmail.com"')
def step_impl(context):
    user_account_page = UserAccountPage(context.driver)
    assert user_account_page.get_email() == "muhammadjaziem26@gmail.com", \
        f"Expected email 'muhammadjaziem26@gmail.com', but got '{user_account_page.get_email()}'"
