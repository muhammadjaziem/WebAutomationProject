Feature: User Login
  As a user, I can log in to VSM using my email and password

  Scenario: Successful login to VSM
    Given the user is on the VSM login page
    When the user clicks the SSO login button
    And the user enters valid credentials
    Then the user should be redirected to the dashboard page
    And the dashboard URL should be "https://vsmonitor.com/dashboard"
