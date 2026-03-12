"""Module """
import hashlib
import json

from .enterprise_project import EnterpriseProject


class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass


    # develop method as you write test cases
    def register_project(self,company_cif: str, project_achronym: str, project_description: str, department: str, date: str, budget: float):
        objProject = EnterpriseProject(company_cif, project_achronym, project_description, department, date, budget) # replace with actual params
        return objProject.project_id
    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True

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
