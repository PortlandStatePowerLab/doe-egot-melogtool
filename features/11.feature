Feature: The output file should be named based on user input
	In order to simplify storage of output files
	As a Test Engineer
	I want the log parser to automatically generate .csv files using output names defined by the user, potentially including the timestamp

Scenario: Output file given a name and timestamp
	Given The options file indicates a specific name should be used for the output file
	And  The options file indicates the timestamp should be appended to the filename
	When The log parser runs
	Then The output filename should be what was written in the options file with a timestamp appended

Scenario: Output file given a name and no timestamp
	Given The options file indicates a specific name should be used for the output file
	And  The options file indicates the timestamp should not be appended to the filename
	When The log parser runs
	Then The output filename should be what was written in the options file

@sean
Scenario: Output file not given a name
	Given The options file does not indicate a specific name for the output file
	When The log parser runs
	Then The output filename should be a timestamp