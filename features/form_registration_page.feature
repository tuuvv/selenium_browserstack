Feature: Form Registration Page

  Background: Open Form Authentication page
    Given I have navigated to the 'practice-auto' "home" page

#  Scenario Outline: Registration Sign in
#    When I click on the '<page>' link
#    Then the '<page>' page opens
#    And a '<username>' input is displayed with label is '<user_label>'
#    And a '<password>' input is displayed with label is '<pass_label>'
#    And a Register button is displayed
#    And I enter a username of '<username>'
#    And I enter a password of '<password>'
#    And I click the Register button
#    And the opening paragraph text is
#      """
#      From your account dashboard you can view your recent orders, manage your shipping and billing addresses and edit your password and account details.
#      """
#    Examples:
#      | username           | user_label      | password | pass_label | page       |
#      | vuvantuu@gmail.com | Email address * | Vvtu_1z3 | Password * | My Account |

#  Scenario Outline: Registration with the invalid email
#    When I click on the '<page>' link
#    Then the '<page>' page opens
#    And I enter a username of '<username>'
#    And I enter a password of '<password>'
#    And I click the Register button
#    And a "Error: Please provide a valid email address." message banner is displayed
#
#    Examples:
#      | username    | password | page       |
#      | vuvantuu@zz | Vvtu_1z3 | My Account |

#  Scenario Outline: Registration with the empty email
#    When I click on the '<page>' link
#    Then the '<page>' page opens
#    And I enter a password of '<password>'
#    And I click the Register button
#    And a "Error: Please provide a valid email address." message banner is displayed
#
#    Examples:
#      | password | page       |
#      | Vvtu_1z3 | My Account |
#
#  Scenario Outline: Registration with the empty password
#    When I click on the '<page>' link
#    Then the '<page>' page opens
#    And I enter a username of '<username>'
#    And I click the Register button
#    And a "Error: Please enter an account password." message banner is displayed
#
#    Examples:
#      | username        | page       |
#      | vuvantuu@aa.com | My Account |

  Scenario Outline: Registration with the empty password
    When I click on the '<page>' link
    Then the '<page>' page opens
    And I click the Register button
    And a "Error: Please provide a valid email address." message banner is displayed

    Examples:
      | page       |
      | My Account |