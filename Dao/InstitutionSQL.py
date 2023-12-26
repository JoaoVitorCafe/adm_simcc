# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys
sys.path.append('../')

import Dao.dbHandler as dbHandler
from Model.Institution import Institution

def insert_institution(institution):
    sql = """
      INSERT INTO institution (name, acronym, email_user, PASSWORD)
      VALUES ('{name}', '{acronym}', '{email_user}', '{password}')
   """.format(
        name=institution.name,
        acronym=institution.acronym,
        email_user=institution.email_user,
        password=institution.password
    )

    return dbHandler.execScript_db(sql)

institution_instance = Institution()
institution_instance.name = "University S"
institution_instance.acronym = "UA"
institution_instance.email_user = "ua@example.com"
institution_instance.password = "password123"

result = insert_institution(institution_instance)

print(result)
