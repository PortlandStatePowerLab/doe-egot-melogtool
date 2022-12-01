Feature: The user can select data by measurement point
	In order to make the ME log data more usable
	As a Test Engineer
	I want there to be an option allowing the user to select one or more measurement points for output

@sean
Scenario: Normal output run
	Given The log parser is configured to output a direct value
	And The input options file is set to produce values based on measurement points
	When The log parser has completed parsing a log
	Then The returned values should contain data from the desired measurement points