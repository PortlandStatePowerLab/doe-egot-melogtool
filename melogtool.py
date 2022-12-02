import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import xmltodict
import time
# import numpy as np
import pandas as pd



class MELogTool:
    """

    """
    def __init__(self):
        self.log_filepath = None
        self.quit_condition = False
        self.file_not_found_error = False
        self.options_import_error = False
        self.log_import_error = False
        self.option_should_output_csv = False
        self.option_output_file_name = None
        self.option_start_time = None
        self.option_end_time = None
        self.option_measurement_points = None
        self.option_keys_to_include = None
        self.option_values_to_search = None
        self.imported_options = None
        self.parsed_log_direct_value = None
        self.include_timestamp = True

    def import_options(self, options_filename):
        try:
            tree = ET.parse(options_filename)
            root = tree.getroot()
            self.imported_options = xmltodict.parse(ET.tostring(root))["options"]
            self.log_filepath = self.imported_options["log_filepath"]
            self.option_should_output_csv = self.imported_options["should_output_csv"]
            self.include_timestamp = self.imported_options["include_timestamp"]
            time_string = time.strftime("%Y%m%d_%H%M%S")
            if self.imported_options['use_file_name'] == 'True':
                self.option_output_file_name = self.imported_options["output_file_name"]
                self.option_output_file_name = self.option_output_file_name + time_string
            else:
                self.option_output_file_name = time_string
            self.option_start_time = self.imported_options["start_time"]
            self.option_end_time = self.imported_options["end_time"]
            if self.imported_options['use_measurement_points'] == 'True':
                self.option_measurement_points = self.imported_options["measurement_points"]
                self.option_measurement_points = self.option_measurement_points.strip('][').split(', ')
            if self.imported_options['use_key_filtering'] == 'True':
                self.option_keys_to_include = self.imported_options["keys_to_include"]
                self.option_keys_to_include = self.option_keys_to_include.strip('][').split(', ')
            if self.imported_options['use_search_function'] == 'True':
                self.option_values_to_search = self.imported_options["values_to_searc"]
                self.option_values_to_search = self.option_values_to_search.strip('][').split(', ')
        except FileNotFoundError:
            self.quit_condition = True
            self.file_not_found_error = True
            print("Error: Options file not found. Quitting...")
            quit()
        except xml.etree.ElementTree.ParseError:
            self.quit_condition = True
            self.options_import_error = True
            print("Error: Unable to parse options input file. Ensure it is in the proper format. Quitting...")
            quit()

    def parse_logs(self, options_filename_arg=None, log_filename_arg=None):
        self.import_options(options_filename_arg)
        if log_filename_arg is not None:
            self.log_filepath = log_filename_arg
        # Read logs
        log_df = pd.read_csv(self.log_filepath)
        # Filter time
        if (self.option_start_time != None) and (self.option_end_time != None):
            timeindex_dict = {}
            for i in log_df.index:
                timeindex_dict[log_df["Timestamp"][i]] = i
            try:
                start_time_index = timeindex_dict[self.option_start_time]
            except KeyError:
                self.quit_condition = True
                self.options_import_error = True
                print("Error: Unable to parse start_time. Ensure it is in the proper format. Quitting...")
                quit()
            try:
                end_time_index = timeindex_dict[self.option_end_time]
            except KeyError:
                self.quit_condition = True
                self.options_import_error = True
                print("Error: Unable to parse end_time. Ensure it is in the proper format. Quitting...")
                quit()
            time_filtered_df = log_df[start_time_index:end_time_index]
        else:
            print("No start/end times given. Using full set.")
            time_filtered_df = log_df

        # Filter columns
        column_filtered_df = time_filtered_df["Timestamp"]
        if self.option_measurement_points is not None:
            for i in self.option_measurement_points:
                column_filtered_df = pd.merge(column_filtered_df, time_filtered_df[i], left_index=True, right_index=True)
        if self.option_values_to_search is not None:
            pass  # Search for contents and pd.merge() column when found. Not implemented.
        if (self.option_measurement_points is None) and (self.option_values_to_search is None):
            print("No columns filtered. Using all measurement points.")
            column_filtered_df = time_filtered_df

        return column_filtered_df

melogtool = MELogTool()
melogtool.parse_logs("options.xml")
