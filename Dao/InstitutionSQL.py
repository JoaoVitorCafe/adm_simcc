# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.Institution import Institution


def insert_institution(institution):
    sql = """
      INSERT INTO adm_institution (name, acronym, email_user, PASSWORD)
      VALUES ('{name}', '{acronym}', '{email_user}', '{password}')
   """.format(
        name=institution.name,
        acronym=institution.acronym,
        email_user=institution.email_user,
        password=institution.password,
    )

    return dbHandler.execScript_db(sql)


def query_institution(ID):
    sql = """
    SELECT * FROM adm_institution WHERE institution_id = {filter}
""".format(
        filter=ID
    )
    return pd.DataFrame(
        dbHandler.consultar_db(sql),
        columns=["institution_id", "name", "acronym", "email_user", "password"],
    )
