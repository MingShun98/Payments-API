Feature: Transactions
  Scenario: Successful money transfer
    Given a user "Alice" with $100 balance
    And a user "Bob" with $50 balance
    When Alice sends $20 to Bob
    Then Alice's balance should be $80
    And Bob's balance should be $70

Scenario: Get an existing user
    Given a user "alice" exists
    When I request GET /users/alice
    Then the response status code should be 200
