Feature: Test the Chhatrabas application
    Scenario: Verify Home page
        Given Launch the browser
        Then verify the page title
        And close the browser

    Scenario: Verify login functionality
        Given Launch the app
        When enter login credentials
        Then click login
        Then verify the page title
        And close the App