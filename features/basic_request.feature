@basic_requests
Feature: Basic Request
    @request @smoke
    Scenario: Basic Request of boards
        Given Defines "GET" request to "/members/me/boards"
        When The request is sent
        #And The schema is validated with "schema.json"
        Then The status code should be 200