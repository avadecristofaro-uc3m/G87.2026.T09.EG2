from unittest import TestCase

from uc3m_consulting import EnterpriseManager


class TestEnterpriseManager(TestCase):
    def test_TC1(self):
        obj=EnterpriseManager()
        # value=obj.register_project() -- fill params with valid cases in excel file
        self.assertEqual(value, "[expected_hash_value]")