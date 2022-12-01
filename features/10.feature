Feature: The log parser determines which options to use based on what’s present or missing from the options input file
	In order to simplify setting options for the log parser
	As a Test Engineer
	I want the log parser to automatically determine which options to use based on the contents of the options input text file

@sean
Scenario: All options used
	Given An options file is provided by argument to the log parser with all options present in the file
	When The log parser runs
	Then The output will be generated correctly

@sean
Scenario: Not all options used
	Given An options file is provided by argument to the log parser with some options not present in the file
	When The log parser runs
	Then The output will be generated correctly