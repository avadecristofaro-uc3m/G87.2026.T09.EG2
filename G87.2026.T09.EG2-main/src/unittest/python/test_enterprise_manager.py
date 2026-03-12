"""Module """
from unittest import TestCase
import hashlib
import json
from pathlib import Path

from uc3m_consulting.enterprise_manager import EnterpriseManager


class TestEnterpriseManager(TestCase):
    """Valid test cases for Method 2: register_document."""

    def test_tc1_valid_pdf(self):
        """TC1: valid PROJECT_ID and valid FILENAME with .pdf extension."""
        manager = EnterpriseManager()

        json_path = (
                Path(__file__).parent
                / "resources"
                / "register_document"
                / "valid"
                / "tc1-valid_pdf.json"
        )

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

        self.assertEqual(expected_result, result)
