Feature: SHOP Page
  Tests for the 'http://practice.automationtesting.in/' shop page

  Background: Open home page
    Given I have navigated to the 'practice-auto' "home" page

  Scenario Outline: Shop - Filter By Price Functionality
    When I click on the '<subpage>' link
    Then the '<subpage>' page opens
    And Adjust the filter by price between 150 to 450 rps
    And I click on the Filter btn
    And all books only between 150 to 450 rps price

    Examples:
      | subpage |
      | Shop    |

  Scenario Outline: Shop - Default Sorting Functionality
    When I click on the '<subpage>' link
    Then the '<subpage>' page opens
    And I select '<option_text>' from the dropdown list
    And the dropdown value is '<option_text>'

    Examples:
      | subpage | option_text     |
      | Shop    | Sort by newness |