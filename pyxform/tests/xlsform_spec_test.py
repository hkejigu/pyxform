"""
Some tests for the new (v0.9) spec is properly implemented.
"""
import unittest2 as unittest
import codecs
import os
import pyxform
from pyxform.errors import PyXFormError
from pyxform.tests.utils import XFormTestCase

DIR = os.path.dirname(__file__)


class MainTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "xlsform_spec_test.xlsx"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        # Get the xform output path:
        root_filename, ext = os.path.splitext(filename)
        output_path = os.path.join(DIR, "test_output", root_filename + ".xml")
        expected_output_path = os.path.join(DIR, "test_expected_output",
                                            root_filename + ".xml")
        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            path_to_excel_file, warnings=warnings)
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, 'rb', encoding="utf-8") \
                as expected_file:
            with codecs.open(output_path, 'rb', encoding="utf-8") \
                    as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class FlatXlsformTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "flat_xlsform_test.xlsx"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        # Get the xform output path:
        root_filename, ext = os.path.splitext(filename)
        output_path = os.path.join(DIR, "test_output", root_filename + ".xml")
        expected_output_path = os.path.join(
            DIR, "test_expected_output", root_filename + ".xml")
        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            path_to_excel_file, warnings=warnings)
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, 'rb', encoding="utf-8") \
                as expected_file:
            with codecs.open(output_path, 'rb', encoding="utf-8") \
                    as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class TestNewWidgets(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "widgets.xls"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        # Get the xform output path:
        root_filename, ext = os.path.splitext(filename)
        output_path = os.path.join(DIR, "test_output", root_filename + ".xml")
        expected_output_path = os.path.join(
            DIR, "test_expected_output", root_filename + ".xml")
        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(path_to_excel_file,
                                                          warnings=warnings)
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, 'rb', encoding="utf-8") \
                as expected_file:
            with codecs.open(output_path, 'rb', encoding="utf-8") \
                    as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class WarningsTest(unittest.TestCase):
    """
    Just checks that the number of warnings thrown when reading warnings.xls
    doesn't change
    """

    def runTest(self):
        filename = "warnings.xls"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        warnings = []
        pyxform.xls2json.parse_file_to_json(
            path_to_excel_file, warnings=warnings)
        self.assertEquals(
            len(warnings), 21, "Found " + str(len(warnings)) + " warnings")


class CalculateWithoutCalculationTest(unittest.TestCase):
    """
    Just checks that calculate field without calculation raises a PyXFormError.
    """

    def runTest(self):
        filename = "calculate_without_calculation.xls"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        self.assertRaises(PyXFormError, pyxform.xls2json.parse_file_to_json,
                          path_to_excel_file)


class PullDataTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "pull_data.xlsx"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        # Get the xform output path:
        root_filename, ext = os.path.splitext(filename)
        output_path = os.path.join(DIR, "test_output", root_filename + ".xml")
        expected_output_path = os.path.join(DIR, "test_expected_output",
                                            root_filename + ".xml")
        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            path_to_excel_file, warnings=warnings)
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(output_path, warnings=warnings)

        # Compare with the expected output:
        with codecs.open(expected_output_path, 'rb', encoding="utf-8") \
                as expected_file:
            with codecs.open(output_path, 'rb', encoding="utf-8") \
                    as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())

        # cleanup
        os.remove(output_path)


class SeachAndSelectTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "search_and_select.xlsx"
        path_to_excel_file = os.path.join(DIR, "example_xls", filename)
        # Get the xform output path:
        root_filename, ext = os.path.splitext(filename)
        output_path = os.path.join(DIR, "test_output", root_filename + ".xml")
        expected_output_path = os.path.join(DIR, "test_expected_output",
                                            root_filename + ".xml")
        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            path_to_excel_file, warnings=warnings)
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(output_path, warnings=warnings)

        # Compare with the expected output:
        with codecs.open(expected_output_path, 'rb', encoding="utf-8") \
                as expected_file:
            with codecs.open(output_path, 'rb', encoding="utf-8") \
                    as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())

        # cleanup
        os.remove(output_path)


if __name__ == '__main__':
    unittest.main()
