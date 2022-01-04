# Created by victo at 11/30/2021
Feature: Test for amazon search


  Scenario: user can search for a product on Amazon
    Given Open Amazon page
    When Search for table
    And Click search icon
    Then Search results have table