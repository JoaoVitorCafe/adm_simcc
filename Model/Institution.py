class Institution(object):
    def __init__(self):
        self.institution_id = None
        self.name = ""
        self.acronym = ""
        self.email_user = ""
        self.password = ""

    def get_json(self):
        institution = {
            'institution_id': str(self.institution_id),
            'name': str(self.name),
            'acronym': str(self.acronym),
            'email_user': str(self.email_user),
            'password': str(self.password),
        }
        
        return institution


institution_instance = Institution()
institution_instance.institution_id = 1
institution_instance.name = "University A"
institution_instance.acronym = "UA"
institution_instance.email_user = "ua@example.com"
institution_instance.password = "password123"
print(institution_instance.get_json())
