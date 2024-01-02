class Institution(object):
    def __init__(self):
        self.institution_id = None
        self.name = ""
        self.acronym = ""
        self.email_user = ""
        self.password = ""

    def get_json(self):
        institution = {
            "institution_id": str(self.institution_id),
            "name": str(self.name),
            "acronym": str(self.acronym),
            "email_user": str(self.email_user),
            "password": str(self.password),
        }

        return institution
