@basic_requests
Feature: Basic Request
    @request @smoke
    Scenario: Basic Request of boards
        Given Defines "GET" request to "/members/me/boards"
        When The request is sent
        #And The schema is validated with "schema.json"
        Then The status code should be 200

    @post2 @fixture.delete.boards
    Scenario: Create a Board
        Given Defines "POST" request to "/boards/"
            | key  |   value   |
            | name |  MyBoard  |
        And The request is sent
        Given Defines "PUT" request to "/boards/<board_id>"
            | key  |   value   |
            | name |  MyBoard  |
        #And The schema is validated with "schema.json"
        Then The status code should be 200
        And Validates response body with
            | key        |  value   |
            | name       | MyBoard  |
            | desc       |          |

    @negative
    Scenario: Create a Board with invalid values
        Given Defines "POST" request to "/boards/"
            |        key       |   value   |
            |        name      |  MyBoard  |
            |        desc      |           |
            | prefs_cardCovers |    None   |
        When The request is sent
        #And The schema is validated with "schema.json"
        Then The status code should be 400
        And Validates response body with
            | key        |               value                |
            | message    | invalid value for prefs_cardCovers |
