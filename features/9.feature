Feature: The log parser imports options from a text file defined in command line arguments
	In order to simplify setting options for the log parser
	As a Test Engineer
	I want the log parser to accept options text files as a command line argument

@sean
Scenario: Proper filename provided
	Given An existing options file is provided by argument to the log parser
	When The log parser runs
	Then A value should be returned

@sean
Scenario: Improper filename provided
	Given A nonexistant options file is provided by argument to the log parser
	When The log parser runs
	Then The log parser should inform the user that the file was not found
	And The program should end