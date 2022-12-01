Feature: The user will set options in an external text file
	In order to simplify setting options for the log parser
	As a Test Engineer
	I want options for each log parser run to be kept in a text file

@sean
Scenario: Options set by user
	Given An options file exists with contents recognizable by the log parser
	When The log parser runs
	Then A value should be returned

@sean
Scenario: Options set improperly by user
	Given An options file exists with contents unrecognizable by the log parser
	When The log parser runs
	Then The log parser should inform the user that the options were improperly set
	And The program should end