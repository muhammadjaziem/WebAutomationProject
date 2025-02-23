Feature: User Account Verification

  Scenario: Verify username and email after login
    Given I am logged into the application
    When I navigate to "My user account"
    Then I should be on the user profile page
    And my firstname and lastname should be "Test" and "Account"
    And my email should be "muhammadjaziem26@gmail.com"
