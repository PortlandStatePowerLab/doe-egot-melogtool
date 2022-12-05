from behave import *
from os import path
import melogtool as melt
import time
import datetime
melogtool = melt.MELogTool()

@given(u'The log parser is configured to output a direct value')
def step_impl(context):
    context.options_file = "options.xml"
    melogtool.import_options(context.options_file)
    print(melogtool.option_should_output_csv)
    assert melogtool.option_should_output_csv == "False"


@when(u'The log parser is called as a function')
def step_impl(context):
    try:
        melogtool.parse_logs(context.options_file, context.logfile)
    except SystemExit:
        assert True is False
    assert melogtool.quit_condition is not True

@when(u'The log parser has completed parsing a log')
def step_impl(context):
    try:
        context.parsed_values = melogtool.parse_logs(context.options_file, context.logfile)
    except SystemExit:
        assert melogtool.quit_condition is not True
        pass

@then(u'A value should be returned')
def step_impl(context):
    assert context.parsed_values is not None


@given(u'An options file is provided by argument to the log parser')
def step_impl(context):
    assert path.exists(
        "/options.xml") is True


@given(u'All options are present in the file')
def step_impl(context):
    context.options_file = "options.xml"
    melogtool.import_options(context.options_file)


@when(u'The log parser runs')
def step_impl(context):
    try:
        context.parsed_values = melogtool.parse_logs(context.options_file, context.logfile)
    except SystemExit:
        pass


@then(u'The output will be generated correctly')
def step_impl(context):
    assert context.parsed_values is not None


@given(u'Some options are not present in the file')
def step_impl(context):
    context.options_file = "options2.xml"
    melogtool.import_options(context.options_file)


@given(u'The options file does not indicate a specific name for the output file')
def step_impl(context):
    context.options_file = "options2.xml"
    melogtool.import_options(context.options_file)


@then(u'The output filename should be a timestamp')
def step_impl(context):
    assert type(time.mktime(datetime.datetime.strptime(melogtool.option_output_file_name,
                                                "%Y%m%d_%H%M%S").timetuple())) is float


@when(u'The log parser runs using an input log file in the proper format')
def step_impl(context):
    context.options_file = "options.xml"
    try:
        context.parsed_values = melogtool.parse_logs(context.options_file, context.logfile)
    except SystemExit:
        assert True is False
    assert melogtool.quit_condition is not True


@when(u'The log parser runs using an input log file in an improper format')
def step_impl(context):
    context.logfile = "options.xml"
    context.options_file = "options.xml"
    try:
        melogtool.parse_logs(context.options_file, context.logfile)
    except SystemExit:
        pass


@then(u'The user is notified that the input log can not be used')
def step_impl(context):
    assert melogtool.log_import_error is True


@then(u'The program stops')
def step_impl(context):
    assert melogtool.quit_condition is True


@given(u'The input options file is set to produce values based on measurement points')
def step_impl(context):
    melogtool.import_options("options.xml")
    assert melogtool.option_measurement_points is not None


@then(u'The returned values should contain data from the desired measurement points')
def step_impl(context):
    #  Note: this test assumes no corner cases, which will arise when search is implemented
        print(len(melogtool.option_measurement_points))
        print(len(context.parsed_values))
        assert len(melogtool.option_measurement_points)*len(melogtool.option_keys_to_include) == len(context.parsed_values)-1

@given(u'An options file is provided by argument to the log parser with all options present in the file')
def step_impl(context):
    context.options_file = "options.xml"
    try:
        melogtool.import_options(context.options_file)
    except SystemExit:
        assert melogtool.quit_condition is True

@given(u'An options file is provided by argument to the log parser with some options not present in the file')
def step_impl(context):
    context.options_file = "options2.xml"
    melogtool.import_options(context.options_file)


@given(u'An existing options file is provided by argument to the log parser')
def step_impl(context):
    context.options_file = "options.xml"
    melogtool.import_options(context.options_file)


@given(u'A nonexistant options file is provided by argument to the log parser')
def step_impl(context):
    context.options_file = "ThisFileDoesNotExist.txt"
    try:
        melogtool.import_options(context.options_file)
    except SystemExit:
        assert melogtool.quit_condition is True


@then(u'The output should be generated without exceptions being raised')
def step_impl(context):
    assert context.parsed_values is not None
    assert melogtool.quit_condition is not True


@given(u'The contents of the options file are not recognizable by the log parser')
def step_impl(context):
    context.options_file = "MeasOutputLogsExample.csv"
    melogtool.import_options(context.options_file)


@then(u'The log parser should inform the user that the options were improperly set')
def step_impl(context):
    assert melogtool.options_import_error is True


@then(u'The program should end')
def step_impl(context):
    assert melogtool.quit_condition is True


@given(u'An options file exists with contents recognizable by the log parser')
def step_impl(context):
    context.options_file = "options.xml"
    melogtool.import_options(context.options_file)


@given(u'An options file exists with contents unrecognizable by the log parser')
def step_impl(context):
    context.options_file = "MeasOutputLogsExample.csv"
    try:
        melogtool.import_options(context.options_file)
    except SystemExit:
        assert melogtool.options_import_error is True

@then(u'The log parser should inform the user that the file was not found')
def step_impl(context):
    assert melogtool.file_not_found_error is True

