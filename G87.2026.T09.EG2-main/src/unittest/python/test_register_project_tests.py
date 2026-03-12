"""class for testing the regsiter_order method"""
import unittest
from uc3m_consulting import EnterpriseManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    def test_TC1( self ):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678","PRO01","ArtQuestXR","HR","01/01/2025",50000.00)
        self.assertEqual(value, "deca2698d32baefe542ef5c3ba8236a2" )



if __name__ == '__main__':
    unittest.main()
