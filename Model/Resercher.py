class Researcher(object):
    def __init__(self):
        self.researcher_id = None
        self.name = ""
        self.lattes_id = ""
        self.institution_id = None  


    def get_json(self):
        researcher = {
            'researcher_id': str(self.researcher_id),
            'name': str(self.name),
            'lattes_id': str(self.lattes_id),
            'institution_id': str(self.institution_id),
        }
        return researcher



researcher_instance = Researcher()
researcher_instance.researcher_id = 1
researcher_instance.name = "John Doe"
researcher_instance.lattes_id = "JD123"
researcher_instance.institution_id = 1


print(researcher_instance.get_json())