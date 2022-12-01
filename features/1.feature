Feature: The log parser produces either logs or values based on user needs
  In order to consolidate functionality into a single script
  As a test engineer
  I want the option to receive either log or direct output

Scenario: Successful run with .csv option set
	Given The log parser is configured to output a .csv
	When The log parser has completed parsing a log
	Then A new .csv file should be generated

Scenario: Successful run with .csv option not set
	Given The log parser is configured to output a value directly
	When The log parser has completed parsing a log
	Then A new .csv file should not be generated

@sean
Scenario: Successful run with function call option set
	Given The log parser is configured to output a direct value
	When The log parser is called as a function
    And The log parser has completed parsing a log
	Then A value should be returned

Scenario: Unsuccessful run with .csv option set
	Given The log parser is configured to output a .csv
	When The log parser has attempted to parse a log
	But A new .csv file is not generated
    Then The user should be informed that a log was not generated
    And Any exception should be delivered to the user

Scenario: Unsuccessful run with function call option set
	Given The log parser is configured to output a direct value
	When The log parser has attempted to parse a log
	But A direct value is not returned
    Then The user should be informed that value was not generated
    And Any exception should be delivered to the user