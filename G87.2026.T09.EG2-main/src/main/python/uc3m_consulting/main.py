#from uc3m_consulting import EnterpriseProject

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import enterprise_project

def showMD5():
    obj= enterprise_project.EnterpriseProject('B86666660','PROJ01','Car sharing beta release','HR','01/01/2026',75000)
    print(obj.project_id)

if __name__ == '__main__':
    showMD5()
# def test():
#     obj = EnterpriseProject() # fill in params w specific test data
#     print(obj.project_id) # produces expected hash value string that you'll put under 'result' tab in excel AND see in TestEnterpriseManager