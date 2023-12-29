class GraduateProgram(object):
    def __init__(self):
        self.graduate_program_id = None
        self.code = str()
        self.name = str()
        self.area = str()
        self.modality = str()
        self.type = str()
        self.rating = str()
        self.institution_id = None
        self.description = str()
        self.url_image = str()

    def get_json(self):
        graduateProgram = {
            "graduate_program_id": str(self.graduate_program_id),
            "code": str(self.code),
            "name": str(self.name),
            "area": str(self.area),
            "modality": str(self.modality),
            "type": str(self.type),
            "rating": str(self.rating),
            "institution_id": str(self.institution_id),
        }
        return graduateProgram
