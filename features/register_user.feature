Feature: Register User

    Scenario: Click on 'Signup / Login' button
        Given Home page is visible successfully
        When User clicks on 'Signup / Login' button
        Then 'New User Signup!' is visible

    Scenario: Enter Account Information
        Given User is on the registration page
        When User enters name and email address and clicks on 'Signup' button
        Then 'ENTER ACCOUNT INFORMATION' is visible

    Scenario: Fill details
        When User fills the details and clicks 'Create Account' button
        Then 'ACCOUNT CREATED!' is visible
        And User clicks on 'Continue' button

    Scenario: Delete Account
        Given 'Logged in as username' is visible
        When User clicks on 'Delete Account' button
        Then 'ACCOUNT DELETED!' is visible
        And User clicks on 'Continue' button
    