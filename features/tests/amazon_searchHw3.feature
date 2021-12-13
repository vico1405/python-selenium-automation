# Created by victor at 12/11/2021
Feature: Open amazon cart, verify is empty


  Scenario:User can verify amazon cart is empty

    Given Open Amazon page
    When Click on cart icon
    Then Amazon cart is empty