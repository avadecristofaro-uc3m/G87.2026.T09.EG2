"""Module """
from unittest import TestCase
from unittest.mock import patch, PropertyMock
import hashlib
import json
from pathlib import Path

from uc3m_consulting.enterprise_manager import EnterpriseManager
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException


class TestRegisterDocument(TestCase):
    """Valid test cases for Method 2: register_document."""

    @staticmethod
    def get_json_path(folder_type: str, json_filename: str):
        """Helper function to get JSON file path for each test case"""
        json_path = (
                Path(__file__).parent
                / "resources"
                / "register_document"
                / folder_type
                / json_filename
        )
        return json_path
    def valid_test_case_algorithm(self, folder_type: str, json_filename: str):
        """Helper function for all valid cases to verify outputs"""
        manager = EnterpriseManager()

        json_path = self.get_json_path(folder_type, json_filename)

        with open(json_path, "r", encoding="utf-8") as file:
            input_data = json.load(file)

        project_id = input_data["PROJECT_ID"]
        file_name = input_data["FILENAME"]

        text_to_hash = (
            f"{{alg:SHA-256, typ:DOCUMENT, "
            f"project_id:{project_id}, file_name:{file_name}}}"
        )

        expected_result = hashlib.sha256(
            text_to_hash.encode("utf-8")
        ).hexdigest()

        result = manager.register_document(str(json_path))
        print("expected result: " + expected_result)
        print("actual result: " + result)

        # Assert Output 1: SHA-256 string
        self.assertEqual(expected_result, result)

        # Assert Output 2: reads all_documents.json and verifies it has correct data
        with open("all_documents.json", "r", encoding="utf-8") as file:
            documents = json.load(file)

        last_document = documents[-1]

        self.assertEqual(last_document["project_id"], project_id)
        self.assertEqual(last_document["file_name"], file_name)
        self.assertEqual(last_document["file_signature"], result)


    def test_tc1_valid_pdf(self):
        """TC1: valid PROJECT_ID and valid FILENAME with .pdf extension."""
        self.valid_test_case_algorithm("valid", "tc1-valid_pdf.json")


    def test_tc2_valid_docx(self):
        """TC2: valid PROJECT_ID and valid FILENAME with .docx extension."""
        self.valid_test_case_algorithm("valid", "tc2-valid_docx.json")

    def test_tc3_valid_xlsx(self):
        """TC3: valid PROJECT_ID and valid FILENAME with .xlsx extension."""
        self.valid_test_case_algorithm("valid", "tc3-valid_xlsx.json")

    def test_tc4_missing_project_id(self):
        """TC4: Invalid JSON from missing PROJECT_ID"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc4-missing_project_id.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: missing <PROJECT_ID>",
            str(context.exception)
        )

    def test_tc5_missing_separator(self):
        """TC5: Invalid JSON from missing SEPARATOR"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc5-missing_separator.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: missing <SEPARATOR>",
            str(context.exception)
        )

    def test_tc6_missing_filename(self):
        """TC6: Invalid JSON from missing FILENAME"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc6-missing_filename.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: missing <FILENAME>",
            str(context.exception)
        )

    def test_tc7_missing_fields(self):
        """TC7: Invalid JSON from missing FIELDS"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc7-missing_fields.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: missing <FIELDS>",
            str(context.exception)
        )

    def test_tc8_duplicate_project_id(self):
        """TC8: Invalid JSON from duplicate <PROJECT_ID>"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc8-duplicate_project_id.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: duplicate field <PROJECT_ID>",
            str(context.exception)
        )

    def test_tc9_duplicate_filename(self):
        """TC9: Invalid JSON from duplicate <FILENAME>"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc9-duplicate_filename.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON does not have the expected structure: duplicate field <FILENAME>",
            str(context.exception)
        )

    def test_tc10_invalid_project_id_label(self):
        """TC10: Invalid JSON from modified field name for project ID"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc10-invalid_project_id_label.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON data has no valid values: invalid PROJECT_ID label",
            str(context.exception)
        )

    def test_tc11_invalid_project_id_value(self):
        """TC11: Invalid JSON from modified project ID value"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc11-invalid_project_id_value.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON data has no valid values: invalid PROJECT_ID value",
            str(context.exception)
        )

    def test_tc12_invalid_name(self):
        """TC12: Invalid JSON from modified file name with non-alphanumeric character"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc12-invalid_name.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON data has no valid values: invalid char in NAME field",
            str(context.exception)
        )

    def test_tc13_invalid_extension(self):
        """TC13: Invalid JSON from modified file name with invalid extension"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc13-invalid_extension.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "JSON data has no valid values: invalid EXTENSION",
            str(context.exception)
        )

    def test_tc14_file_does_not_exist(self):
        """TC14: Invalid from referencing a JSON path that does not exist"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc14-file_does_not_exist.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "Input file not found.",
            str(context.exception)
        )

    def test_tc15_invalid_json_format(self):
        """TC15: Invalid JSON format from missing curly bracket"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc15-invalid_json_format.json")

        with self.assertRaises(EnterpriseManagementException) as context:
            manager.register_document(str(json_path))

        self.assertEqual(
            "The file is not JSON formatted.",
            str(context.exception)
        )

    def test_tc16_internal_processing_error(self):
        """TC16: Invalid case by forcing an internal processing error"""
        manager = EnterpriseManager()
        json_path = self.get_json_path("invalid", "tc16-valid_for_signature_error.json")

        with patch(
                "uc3m_consulting.enterprise_manager.ProjectDocument.file_signature",
                new_callable=PropertyMock,
                side_effect=Exception("Forced signature error")
        ):
            with self.assertRaises(EnterpriseManagementException) as context:
                manager.register_document(str(json_path))

        self.assertEqual(
            "Internal processing error when getting the file_signature.",
            str(context.exception)
        )
