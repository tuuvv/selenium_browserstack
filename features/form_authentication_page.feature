Feature: Form Authentication Page

  Background: Open Form Authentication page
    Given I have navigated to the 'practice-auto' "home" page

  Scenario Outline: Login with valid credentials
    When I click on the '<page>' link
    Then the '<page>' page opens
    And a '<username>' input is displayed with label is '<user_label>'
    And a '<password>' input is displayed with label is '<pass_label>'
    And a Login button is displayed
    And I enter a username of '<username>'
    And I enter a password of '<password>'
    And I click the Login button
    And the opening paragraph text is
      """
      From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details.
      """
    Examples:
      | username  | user_label                  | password | pass_label | page       |
      | tuuvv.uit | Username or email address * | Vvtu_1z3 | Password * | My Account |

  Scenario Outline: Login with invalid username but invalid password
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a username of '<username>'
    And I enter a password of '<password>'
    And I click the Login button
    And a "ERROR: Invalid username. Lost your password?" message banner is displayed

    Examples:
      | page       | username        | password        |
      | My Account | invalidPassword | invalidUsername |

  Scenario Outline: Login with valid username but no password
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a username of '<username>'
    And I click the Login button
    And a "Error: Password is required." message banner is displayed

    Examples:
      | page       | username  |
      | My Account | tuuvv.uit |

  Scenario Outline: Login with valid password but no username
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a password of '<password>'
    And I click the Login button
    And a "Error: Username is required." message banner is displayed

    Examples:
      | page       | password |
      | My Account | Vvtu_1z3 |

  Scenario Outline: Login without user credentials
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I click the Login button
    And a "Error: Username is required." message banner is displayed

    Examples:
      | page       |
      | My Account |

  Scenario Outline: Password should be masked
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a password of '<password>'
    And password field should display the characters in asterisks or bullets

    Examples:
      | page       | password |
      | My Account | Vvtu_1z3 |

  Scenario Outline: Login-Handles case sensitive
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a username of '<username>'
    And I enter a password of '<password>'
    And I click the Login button
    And a "ERROR: The password you entered for the username Tuuvv.uit is incorrect. Lost your password?" message banner is displayed

    Examples:
      | page       | username  | password |
      | My Account | Tuuvv.uit | vvtu_1z3 |

  Scenario Outline: Login-Authentication
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I enter a username of '<username>'
    And I enter a password of '<password>'
    And I click the Login button
    And I click on the '<signout>' link
    And the title login text is correct


    Examples:
      | page       | username  | password | signout  |
      | My Account | tuuvv.uit | Vvtu_1z3 | Sign out |



