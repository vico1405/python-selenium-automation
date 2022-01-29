Feature: Test for loop on bestseller link

  Scenario: User can click on on links on bestseller page
    Given Open Amazon bestsellers page
    When Click on bestseller link on top menu
#    And Click on each top link
    Then Verify correct page opens