# Created by victo at 12/22/2021
Feature: Test to add watch in a cart on Amazon
  # Enter feature description here

  Scenario: Users can add watch product to cart
    Given Open Amazon Page
    When Search for Men's watch
    And Click search icon
    And Click on the first product
    When Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product
