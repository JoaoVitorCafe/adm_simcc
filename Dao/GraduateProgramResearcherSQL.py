# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.GraduateProgram import GraduateProgram


def insert(GraduateProgram):
    sql = """
    INSERT INTO graduate_program_researcher (graduate_program_id, researcher_id, year, type_)
    VALUES
        ('{graduate_program_id}', '{researcher_id}', '{year}', '{type_}')
    """.format(
        graduate_program_id=GraduateProgram.graduate_program_id,
        researcher_id=GraduateProgram.researcher_id,
        year=GraduateProgram.year,
        type_=GraduateProgram.type_,
    )

    return dbHandler.execScript_db(sql)


def query(ID):
    sql = """
    SELECT * FROM graduate_program_researcher WHERE graduate_program_id = {filter}
""".format(
        filter=ID
    )
    return pd.DataFrame(
        dbHandler.consultar_db(sql),
        columns=[
            "graduate_program_id",
            "researcher_id",
            "year",
            "type_",
        ],
    )
