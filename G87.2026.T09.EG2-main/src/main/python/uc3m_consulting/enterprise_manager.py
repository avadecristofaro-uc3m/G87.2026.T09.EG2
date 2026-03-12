"""Module """
import hashlib
import json
import re

from datetime import datetime

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
                company_cif=company_cif,
                project_acronym=project_achronym,
                project_description=project_description,
                department=department,
                starting_date=date,
                project_budget=budget
            )
        except Exception as exc:
            raise EnterpriseManagementException("Error creating project") from exc

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

    def register_document(self, input_file: str):
        """RETURNS SHA-256 SIGNATURE STRING AND JSON FILE
        IF SUCCESSFUL, OR ENTERPRISEMANAGEMENTEXCEPTION
        IN OTHER CASE"""
        with open(input_file, "r", encoding="utf-8") as file:
            input_data = json.load(file)

        project_id = input_data["PROJECT_ID"]
        file_name = input_data["FILENAME"]

        text_to_hash = (
            f"{{alg:SHA-256, typ:DOCUMENT, "
            f"project_id:{project_id}, file_name:{file_name}}}"
        )

        return hashlib.sha256(text_to_hash.encode("utf-8")).hexdigest()
