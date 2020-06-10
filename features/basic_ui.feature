@basic_ui
Feature: Basic UI of Trello

    # @fixture.delete.boards
    Scenario: Create Board
        Given the "admin" user signs in
        When the user clicks on "Create Board" button
        And the user creates Board with
            |     key    |  value  |
            | BoardTitle | BoardUI |
        Then the following board info must appears in Board Details
            |     key    |     value    |
            | BoardTitle |    BoardUI   |
            |   Privacy  | Team Visible |
