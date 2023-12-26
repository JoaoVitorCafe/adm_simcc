class GraduateProgram(object):
    def __init__(self):
        self.graduate_program_id = None
        self.code = ""
        self.name = ""
        self.area = ""
        self.modality = ""
        self.program_type = ""
        self.rating = ""
        self.institution_id = None

    def get_json(self):
        graduate_program = {
            'graduate_program_id': str(self.graduate_program_id),
            'code': str(self.code),
            'name': str(self.name),
            'area': str(self.area),
            'modality': str(self.modality),
            'program_type': str(self.program_type),
            'rating': str(self.rating),
            'institution_id': str(self.institution_id),
        }
        return graduate_program
    
graduate_program_instance = GraduateProgram()
graduate_program_instance.graduate_program_id = 1
graduate_program_instance.code = "GP001"
graduate_program_instance.name = "Computer Science"
graduate_program_instance.area = "Computer Science"
graduate_program_instance.modality = "Master"
graduate_program_instance.program_type = "MSc"
graduate_program_instance.rating = "A"
graduate_program_instance.institution_id = 1
print(graduate_program_instance.get_json())