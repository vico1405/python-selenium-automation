# Created by victo at 11/30/2021
Feature: Test for amazon search


  Scenario: user can search for a product on Amazon
    Given Open Amazon page
    When Search for table
    And Click search icon
#    Then Search results have "table"

  Scenario Outline: User can search for a product
    Given Open Amazon Page
    When Search for <product>
    And Click on search icon
    Then Search result have <expected_result>
    Examples:
    |product  |expected_result    |
    |coffee   |"coffee"           |
    |table    |"table"            |


  Scenario: User can add a product to the cart
    Given Open Amazon Page
    When Search for keyword
    And Click search icon
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product