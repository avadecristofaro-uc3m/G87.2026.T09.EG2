from uc3m_consulting import EnterpriseProject

def test():
    obj = EnterpriseProject() # fill in params w specific test data
    print(obj.project_id) # produces expected hash value string that you'll put under 'result' tab in excel AND see in TestEnterpriseManager