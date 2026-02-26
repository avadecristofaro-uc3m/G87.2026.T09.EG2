# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import enterprise_project

def showMD5():
    obj= enterprise_project.EnterpriseProject('B12345678','PRO01','ArtQuestXR','HR','01/01/2025',999999.99)
    print(obj.project_id)

if __name__ == '__main__':
    showMD5()
