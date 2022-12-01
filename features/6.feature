Feature: The user can select data by searching each cell’s contents for a required value
	In order to make the ME log data more usable
	As a Test Engineer
	I want there to be an option allowing the user to select one or more dictionary values which the log parser can search each cell in the logs for

Scenario: Contents detected
	Given The log parser is configured to output a direct value
	And The input options file is set to produce values based on the detection of contents in a cell
	When The log parser has completed parsing a log
	Then The output values should contain data from each measurement point that includes the contents detected

Scenario: Contents not detected
	Given The log parser is configured to output a direct value
	And The input options file is set to produce values based on the detection of contents in a cell
	And The input options file is set to detect values that do not exist
	When The log parser has completed parsing a log
	Then The log parser should inform the user that no values were detected