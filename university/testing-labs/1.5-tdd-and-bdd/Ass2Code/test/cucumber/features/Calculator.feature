Feature: Simple Calculator

Scenario: Calculator initialisation
    Given a calculator
    When turned on
    Then accumulator should be 0.0
    And there should be no error
    And the accumulator should not be updated
