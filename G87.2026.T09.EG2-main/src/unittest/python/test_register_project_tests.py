"""class for testing the regsiter_order method"""
import unittest
from uc3m_consulting import EnterpriseManager
from uc3m_consulting import EnterpriseManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    def test_tc1( self ):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678","PRO01","ArtQuestXR","HR","01/01/2025",50000.00)
        self.assertEqual(value, "deca2698d32baefe542ef5c3ba8236a2" )

    def test_tc2(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO011", "ArtQuestXR", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "f5155610659bc5c9e5cc9a4e4ed8dd5f")

    def test_tc3(self):
        """valid test case"""
        obj = (EnterpriseManager())
        value = obj.register_project("B12345678", "PRO011111", "ArtQuestXR", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "c8762cb180bba9f3fb00cf08564c6e1d")

    def test_tc4(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO0111111", "ArtQuestXR", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "61e52b2aac90373ac3da6731cf5826f9")

    def test_tc5(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "Urban LabX!", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "d712e19c33ff96346b4fb8003baa21cf")

    def test_tc6(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "Interactive art learning tool", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "f827363943ff8e53e5ac73c0dd8338b7")

    def test_tc7(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "Digital storytelling workshop!", "HR", "01/01/2025", 50000.00)
        self.assertEqual(value, "6e3faf4a0fa507de008822b4f9b2a9cd")

    def test_tc8(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "FINANCE", "01/01/2025", 50000.00)
        self.assertEqual(value, "4aeee0506bd332c9c42a7fc40843ef1e")

    def test_tc9(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "LEGAL", "01/01/2025", 50000.00)
        self.assertEqual(value, "a9dfb82727aef9c0ea0f4cb7dd23470e")

    def test_tc10(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "LOGISTICS", "01/01/2025", 50000.00)
        self.assertEqual(value, "df215fd6a2658c09dcfd2385a6937749")

    def test_tc11(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "02/01/2025", 50000.00)
        self.assertEqual(value, "6b34f2c8301b864b6cc2dc90bf97efce")

    def test_tc12(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "30/01/2025", 50000.00)
        self.assertEqual(value, "249dce3e182a33ebd6461cc5932ae74d")

    def test_tc13(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "31/01/2025", 50000.00)
        self.assertEqual(value, "89f30135f795cb371c804f74741f31e9")

    def test_tc14(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/02/2025", 50000.00)
        self.assertEqual(value, "bd5a3b3e8b36bcced6b0845e8596728d")

    def test_tc15(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/11/2025", 50000.00)
        self.assertEqual(value, "84ceb207721a863f61f15d45e6e73f4c")

    def test_tc16(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/12/2025", 50000.00)
        self.assertEqual(value, "1326973451ce69a7a9fd60752c267039")

    def test_tc17(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2026", 50000.00)
        self.assertEqual(value, "165f4337a4228d64d1cfaf7126ce860a")

    def test_tc18(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2027", 50000.00)
        self.assertEqual(value, "a7ebfdec6047a83208d3c6a5bd62bab1")

    def test_tc19(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 50000.01)
        self.assertEqual(value, "72f8671441e6da4db62d34df6957989f")

    def test_tc20(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 999999.99)
        self.assertEqual(value, "fd59cbf6b511d7172a0487089f22b523")

    def test_tc21(self):
        """valid test case"""
        obj = EnterpriseManager()
        value = obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)
        self.assertEqual(value, "1ce6af3f1664e79e53d418c7eaaef07d")

    def test_tc22(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project(12, "PRO01", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid CIF", str(cm.exception))

    def test_tc23(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid CIF", str(cm.exception))

    def test_tc24(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("1234567810", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid CIF", str(cm.exception))

    def test_tc25(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", 12, "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project acronym", str(cm.exception))

    def test_tc26(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO0", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project acronym", str(cm.exception))

    def test_tc27(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01111111", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project acronym", str(cm.exception))

    def test_tc28(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO0!", "ArtQuestXR", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project acronym", str(cm.exception))

    def test_tc29(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "Code LabX", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project description", str(cm.exception))

    def test_tc30(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "Immersive coding workshop hub!!", "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project description", str(cm.exception))

    def test_tc31(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", 12, "HR", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid project description", str(cm.exception))

    def test_tc32(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", 12, "01/01/2025", 1000000.00)

        self.assertEqual("Invalid department", str(cm.exception))

    def test_tc33(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "other", "01/01/2025", 1000000.00)

        self.assertEqual("Invalid department", str(cm.exception))

    def test_tc34(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", 12, 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc35(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "1/1/2025", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc36(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "00/01/2025", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc37(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "32/01/2025", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc38(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/00/2025", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc39(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/13/2025", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc40(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2024", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc41(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2028", 1000000.00)

        self.assertEqual("Invalid date", str(cm.exception))

    def test_tc42(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", "string")

        self.assertEqual("Invalid budget", str(cm.exception))

    def test_tc43(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 49999.99)

        self.assertEqual("Invalid budget", str(cm.exception))

    def test_tc44(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 1000000.01)

        self.assertEqual("Invalid budget", str(cm.exception))

    def test_tc45(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 53123)

        self.assertEqual("Invalid budget", str(cm.exception))

    def test_tc46(self):
        """invalid test case"""
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            obj.register_project("B12345678", "PRO01", "ArtQuestXR", "HR", "01/01/2025", 5234523.1)

        self.assertEqual("Invalid budget", str(cm.exception))


if __name__ == '__main__':
    unittest.main()
