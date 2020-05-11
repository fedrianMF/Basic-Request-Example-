@Example
Feature: Behave example
    @bvt @smoke
    Scenario: Example test with datatable
        Given The numbers are set
            | number1 | number2 |
            |  1264   |  1736   |
        When These numbers are added up
        Then the result is "3000"

    Scenario: Example test 1
        Given The numbers "8" and "4" are set
        When These numbers are added up
        Then the result is "11"

    Scenario: Example test 2
        Given The numbers "7" and "1" are set
        When These numbers are added up
        Then the result is "8"

    Scenario Outline: Example test using table
        Given The numbers "<first>" and "<second>" are set
        When These numbers are added up
        Then the result is "<result>"

        Examples: Random Numbers
            | first  | second  | result |
            | 1      | 4       | 5      |
            | 2      | 6       | 8      |
