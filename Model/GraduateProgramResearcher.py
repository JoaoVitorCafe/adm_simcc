class GraduateProgramResearcher(object):
    def __init__(self):
        self.graduate_program_id = None
        self.researcher_id = None
        self.year = None
        self.type_ = ""

    def get_json(self):
        graduate_program_researcher = {
            'graduate_program_id': str(self.graduate_program_id),
            'researcher_id': str(self.researcher_id),
            'year': str(self.year),
            'type_': str(self.type_),
        }
        return graduate_program_researcher
    

graduate_program_researcher_instance = GraduateProgramResearcher()
graduate_program_researcher_instance.graduate_program_id = 1
graduate_program_researcher_instance.researcher_id = 1
graduate_program_researcher_instance.year = 2022
graduate_program_researcher_instance.type_ = "Supervisor"
print(graduate_program_researcher_instance.get_json())