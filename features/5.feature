Feature: The user can select data by timestamp
	In order to make the ME log data more usable
	As a Test Engineer
	I want there to be an option allowing the user to select one or more timestamps for output

Scenario: Normal .csv output run
	Given The log parser is configured to output a direct value
	And The input options file is set to produce values based on a range of timestamps
	When The log parser has completed parsing a log
	Then The output values should contain data from the desired range of timestamps