# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.Resercher import Researcher


def insert(Researcher):
    sql = """
      INSERT INTO researcher (researcher_id, name, lattes_id, institution_id)
      VALUES ('{researcher_id}', '{name}', '{lattes_id}', '{institution_id}')
   """.format(
        researcher_id=Researcher.researcher_id,
        name=Researcher.name,
        lattes_id=Researcher.lattes_id,
        institution_id=Researcher.institution_id,
    )

    return dbHandler.execScript_db(sql)


def query(ID):
    sql = """
    SELECT * FROM researcher WHERE institution_id = {filter}
""".format(
        filter=ID
    )
    return pd.DataFrame(
        dbHandler.consultar_db(sql),
        columns=["researcher_id", "name", "lattes_id", "institution_id"],
    )
