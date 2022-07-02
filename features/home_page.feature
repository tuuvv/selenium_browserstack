Feature: Home Page
  Tests for the 'http://practice.automationtesting.in/' home page

  Background: Open home page
    Given I have navigated to the 'practice-auto' "home" page

#  Scenario Outline: Home page three slides only
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And  I click Home button
#    And the '<page>' page opens
#    And Total imgs of slider must be three
#
#    Examples:
#      | subpage | page |
#      | Shop    | Home |
#
#  Scenario Outline: Home page three arrivals only
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And  I click Home button
#    And the '<page>' page opens
#    And Total arrivals must be three
#
#    Examples:
#      | subpage | page |
#      | Shop    | Home |
#
#  Scenario Outline: Home page - Images in Arrivals should navigate
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And  I click Home button
#    And the '<page>' page opens
#    And Total arrivals must be three
#    And I click on the images of arrival
#    And the product page opens
#
#    Examples:
#      | subpage | page |
#      | Shop    | Home |

#  Scenario Outline: Home page - Arrivals images description
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And  I click Home button
#    And the '<page>' page opens
#    And Total arrivals must be three
#    And I click on the images of arrival
#    And the product page opens
#    And I click on the Description tab
#    And description regarding that book the user clicked on
#
#    Examples:
#      | subpage | page |
#      | Shop    | Home |

#  Scenario Outline: Home page - Add to basket
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And I click on the product add btn
#    And the product must added to basket
#
#    Examples:
#      | subpage |
#      | Shop    |

#  Scenario Outline: Home page - Add to basket more book
#    When I click on the '<subpage>' link
#    Then the '<subpage>' page opens
#    And I click on the images of arrival
#    And the product page opens
#    And fill in total product input value 7653 and click product add btn
#    And a "You cannot add that amount to the cart — we have 7653 in stock and you already have 7653 in your cart." message banner is displayed
#
#    Examples:
#      | subpage |
#      | Shop    |

  Scenario Outline: Home page - Arrials - add to basket  -items
    When I click on the '<subpage>' link
    Then the '<subpage>' page opens
#    And I click on the product add btn
#    And the product must added to basket
#    And I click on the item menu
#    And basket page must be open
#    And I click on proceed to checkout btn
#    And checkout page must be open

    Examples:
      | subpage |
      | Shop    |