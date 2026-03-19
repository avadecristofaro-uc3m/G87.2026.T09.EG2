"""Module """
import json
import re
import os

from datetime import datetime

from . import ProjectDocument
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException


class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    VALID_DEPARTMENTS = {"HR", "FINANCE", "LEGAL", "LOGISTICS"}

    # develop method as you write test cases
    def register_project(
            self,
            company_cif: str,
            project_achronym: str,
            project_description: str,
            department: str,
            date: str,
            budget: float
    ) -> str:
        """Registers a project and returns its project id."""

        self._validate_company_cif(company_cif)
        self._validate_project_acronym(project_achronym)
        self._validate_project_description(project_description)
        self._validate_department(department)
        self._validate_date(date)
        self._validate_budget(budget)

        try:
            project = EnterpriseProject(
                # raise exception if CIF is invalid
                company_cif=company_cif,
                # raise exception if achronym is invalid
                project_acronym=project_achronym,
                # raise exception if description is invalid
                project_description=project_description,
                # raise exception if department is invalid
                department=department,
                # raise exception if date is invalid
                starting_date=date,
                # raise exception if budget is invalid
                project_budget=budget
            )
        except Exception as exc:
            raise EnterpriseManagementException("Error creating project") from exc

        # Check for JSON output file with project data
        file_path = "corporate_operations.json"
        try:
            if os.path.exists(file_path):
                with open(file_path, "r") as infile:
                    data_list = json.load(infile)
            else:
                data_list = []

            # Convert project to JSON obj
            project_data = project.to_json()

            data_list.append(project_data)

            # Write back to file
            with open(file_path, "w", encoding="utf-8") as outfile:
                json.dump(data_list, outfile, indent=4)


        except (FileNotFoundError, PermissionError, OSError) as exc:
            raise EnterpriseManagementException("File not found") from exc

        return project.project_id

    @staticmethod
    def _validate_company_cif(company_cif: str) -> None:
        """Validates CIF format: Letter + 7 digits + control."""
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Invalid CIF")

        if not re.fullmatch(r"[A-Z]\d{7}[A-Z0-9]", company_cif):
            raise EnterpriseManagementException("Invalid CIF")

    @staticmethod
    def _validate_project_acronym(project_achronym: str) -> None:
        """Validates acronym length and allowed characters."""
        if not isinstance(project_achronym, str):
            raise EnterpriseManagementException("Invalid project acronym")

        if not re.fullmatch(r"[A-Z0-9]{5,10}", project_achronym):
            raise EnterpriseManagementException("Invalid project acronym")

    @staticmethod
    def _validate_project_description(project_description: str) -> None:
        """Validates description length."""
        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Invalid project description")

        if len(project_description) < 10 or len(project_description) > 30:
            raise EnterpriseManagementException("Invalid project description")

    def _validate_department(self, department: str) -> None:
        """Validates department."""
        if department not in self.VALID_DEPARTMENTS:
            raise EnterpriseManagementException("Invalid department")

    @staticmethod
    def _validate_date(date: str) -> None:
        """Validates date format and allowed years."""
        if not isinstance(date, str):
            raise EnterpriseManagementException("Invalid date")

        if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", date):
            raise EnterpriseManagementException("Invalid date")

        try:
            parsed_date = datetime.strptime(date, "%d/%m/%Y")
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid date") from exc

        if parsed_date.year < 2025 or parsed_date.year > 2027:
            raise EnterpriseManagementException("Invalid date")

    @staticmethod
    def _validate_budget(budget: float) -> None:
        """Validates project budget."""
        if not isinstance(budget, float):
            raise EnterpriseManagementException("Invalid budget")

        if budget < 50000.00 or budget > 1000000.00:
            raise EnterpriseManagementException("Invalid budget")

        if round(budget, 2) != budget:
            raise EnterpriseManagementException("Invalid budget")

    @staticmethod
    def _json_object_pairs_hook(pairs):
        """Parse JSON while detecting duplicate fields."""
        seen_keys = set()
        data = {}

        for key, value in pairs:
            if key in seen_keys:
                if key == "PROJECT_ID":
                    raise EnterpriseManagementException(
                        "JSON does not have the expected structure: duplicate field <PROJECT_ID>"
                    )
                if key == "FILENAME":
                    raise EnterpriseManagementException(
                        "JSON does not have the expected structure: duplicate field <FILENAME>"
                    )
            seen_keys.add(key)
            data[key] = value

        if not data:
            raise EnterpriseManagementException(
                "JSON does not have the expected structure: missing <FIELDS>"
            )

        return data

    @staticmethod
    def _validate_document_project_id(project_id: str) -> None:
        if not isinstance(project_id, str) or not re.fullmatch(r"[0-9a-fA-F]{32}", project_id):
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid PROJECT_ID value"
            )

    @staticmethod
    def _validate_document_filename(file_name: str) -> None:
        if not isinstance(file_name, str):
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid EXTENSION"
            )

        parts = file_name.split(".")
        if len(parts) != 2:
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid EXTENSION"
            )

        name, extension = parts[0], "." + parts[1]

        if not re.fullmatch(r"[A-Za-z0-9]{8}", name):
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid char in NAME field"
            )

        if extension not in {".pdf", ".docx", ".xlsx"}:
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid EXTENSION"
            )

    def register_document(self, input_file: str) -> str:
        """Registers a document and returns its SHA-256 signature."""
        try:
            with open(input_file, "r", encoding="utf-8") as file:
                input_data = json.load(
                    file,
                    object_pairs_hook=self._json_object_pairs_hook
                )
        except FileNotFoundError as exc:
            raise EnterpriseManagementException("Input file not found.") from exc
        except json.JSONDecodeError as exc:
            if "Expecting ',' delimiter" in str(exc):
                raise EnterpriseManagementException(
                    "JSON does not have the expected structure: missing <SEPARATOR>"
                ) from exc
            raise EnterpriseManagementException("The file is not JSON formatted.") from exc

        keys = set(input_data.keys())

        if not keys:
            raise EnterpriseManagementException(
                "JSON does not have the expected structure: missing <FIELDS>"
            )

        if "PROJECT_ID" not in input_data:
            if keys == {"FILENAME"}:
                raise EnterpriseManagementException(
                    "JSON does not have the expected structure: missing <PROJECT_ID>"
                )
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid PROJECT_ID label"
            )

        if "FILENAME" not in input_data:
            if keys == {"PROJECT_ID"}:
                raise EnterpriseManagementException(
                    "JSON does not have the expected structure: missing <FILENAME>"
                )
            raise EnterpriseManagementException(
                "JSON data has no valid values: invalid FILENAME label"
            )

        project_id = input_data["PROJECT_ID"]
        file_name = input_data["FILENAME"]

        self._validate_document_project_id(project_id)
        self._validate_document_filename(file_name)

        try:
            document = ProjectDocument(project_id, file_name)
            file_signature = document.file_signature
        except Exception as exc:
            raise EnterpriseManagementException(
                "Internal processing error when getting the file_signature."
            ) from exc

        try:
            try:
                with open("all_documents.json", "r", encoding="utf-8") as file:
                    all_documents = json.load(file)
                    if not isinstance(all_documents, list):
                        all_documents = []
            except FileNotFoundError:
                all_documents = []

            all_documents.append(document.to_json())

            with open("all_documents.json", "w", encoding="utf-8") as file:
                json.dump(all_documents, file, indent=4)
        except Exception as exc:
            raise EnterpriseManagementException(
                "Internal processing error when getting the file_signature."
            ) from exc

        return file_signature
