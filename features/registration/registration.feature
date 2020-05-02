@web
Feature: User can do registration with valid data

  Scenario: Registration with valid data (with out  POM)
    Given I have valid data for registration
    And I navigate to registration page
    Then I fill registration form
    And I click on submit

  Scenario: Registration with valid data (with POM)
    Given I have valid data for registration
    And I navigate to registration page
    Then I fill registration form with pom
    And I click on submit
