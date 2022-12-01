Feature: The output .csv is two dimensional
	In order to make the ME log data more usable
	As a Test Engineer
	I want log parser output logs to be in a two dimensional format where each cell contains a single value

Scenario: Normal .csv output run
	Given The log parser is configured to output a .csv
	When The log parser has completed parsing a log
	Then Each cell in the log parser should contain a single value