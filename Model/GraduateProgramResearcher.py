class GraduateProgramResearcher(object):
    def __init__(self):
        self.graduate_program_id = None
        self.researcher_id = None
        self.year = None
        self.type_ = ""

    def get_json(self):
        graduate_program_researcher = {
            "graduate_program_id": str(self.graduate_program_id),
            "researcher_id": str(self.researcher_id),
            "year": str(self.year),
            "type_": str(self.type_),
        }
        return graduate_program_researcher
