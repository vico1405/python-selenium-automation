# Created by victor at 12/11/2021
Feature:Tests for cancelling order on Amazon

  Scenario: User can cancel products ordered on amazon

    Given Open Amazon page
    When Click on customer service
    And Search cancel order
    And Click search icon
    Then Cancel items or Orders page display