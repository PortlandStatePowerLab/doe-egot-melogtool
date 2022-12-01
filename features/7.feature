Feature: For each cell captured, the user can select which data is collected
	In order to make the ME log data more usable
	As a Test Engineer
	I want there to be an option allowing the user to select one or more dictionary keys to be output for each cell

Scenario: Normal output run
	Given The log parser is configured to output a direct value
	And The input options file is set to filter the produced output to specific contents
	When The log parser has completed parsing a log
	Then The output values will contain a column for each content specified in the options
	And The output values will not contain a column for any information filtered by the options