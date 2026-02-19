"""Module """
from uc3m_consulting import EnterpriseProject


class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass


    # develop method as you write test cases
    def register_project(company_cif: str, project_achronym: str, project_description: str, department: str, date: str, budget: float):
        objProject = EnterpriseProject(company_cif, project_achronym, project_description, department, date, budget) # replace with actual params
        return objProject.project_id
    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True
