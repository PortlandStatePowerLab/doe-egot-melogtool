from behave import *
from os import path
import melogtool

@given(u'The log parser is configured to output a direct value')
def step_impl(context):
    context.options_file = "options.txt"
    melogtool.import_options(context.options_file)
    assert melogtool.should_output_csv is False

@when(u'The log parser is called as a function')
def step_impl(context):
    melogtool.parse_logs(context.options_file)

@when(u'The log parser has completed parsing a log')
def step_impl(context):
    context.parsed_values = melogtool.parse_logs(context.options_file)
    assert melogtool.quit_condition is not True


@then(u'A value should be returned')
def step_impl(context):
    assert context.parsed_values is not None


@given(u'An options file is provided by argument to the log parser')
def step_impl(context):
    assert path.exists(
        "/home/seanjkeene/PycharmProjects/doe-egot-melogtool/options.txt") is True

@given(u'All options are present in the file')
def step_impl(context):
    context.options_file = "options.txt"
    melogtool.import_options(context.options_file)


@when(u'The log parser runs')
def step_impl(context):
    context.parsed_values = melogtool.parse_logs(context.options_file)
    assert melogtool.quit_condition is not True

@then(u'The output will be generated correctly')
def step_impl(context):
    assert context.parsed_values is not None


@given(u'Some options are not present in the file')
def step_impl(context):
    context.options_file = "options2.txt"
    melogtool.import_options(context.options_file)


@given(u'The options file does not indicate a specific name for the output file')
def step_impl(context):
    context.options_file = "options2.txt"
    melogtool.import_options(context.options_file)
    assert melogtool.option_file_name is None

@then(u'The output filename should be the current timestamp')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The output filename should be the current timestamp')


@given(u'An input log file is provided to the log parser in the proper format')
def step_impl(context):
    melogtool.import_me_log("MeasOutputLogsExample.csv")


@given(u'An input log file is provided to the log parser in an unusable format')
def step_impl(context):
    melogtool.import_me_log("options.txt")


@then(u'The user is notified that the input log can not be used')
def step_impl(context):
    assert melogtool.log_import_error is True

@then(u'The program stops')
def step_impl(context):
    assert melogtool.quit_condition is True

@given(u'The input options file is set to produce values based on measurement points')
def step_impl(context):
    melogtool.import_options("options.txt")
    assert melogtool.measurement_points_to_include is not None

@then(u'The returned values should contain data from the desired measurement points')
def step_impl(context):
    melogtool.parse_logs("options.txt")
    raise NotImplementedError(u'STEP: Then The returned values should contain data from the desired measurement points.')

@given(u'An options file is provided by argument to the log parser with all options present in the file')
def step_impl(context):
    context.options_file = "options.txt"
    melogtool.import_options(context.options_file)

@given(u'An options file is provided by argument to the log parser with some options not present in the file')
def step_impl(context):
    context.options_file = "options2.txt"
    melogtool.import_options(context.options_file)

@given(u'An existing options file is provided by argument to the log parser')
def step_impl(context):
    context.options_file = "options.txt"
    melogtool.import_options(context.options_file)

@given(u'A nonexistant options file is provided by argument to the log parser')
def step_impl(context):
    context.options_file = "ThisFileDoesNotExist.txt"
    melogtool.import_options(context.options_file)

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



