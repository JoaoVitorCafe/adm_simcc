# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.sgbdSQL as sgbdSQL
import pandas as pd
from Model.GraduateProgramAdm import GraduateProgram


def insert_GpResearcher(GraduateProgram):
    sql = """
    INSERT INTO adm_graduate_program_researcher (graduate_program_id, researcher_id, year, type_)
    VALUES
        ('{graduate_program_id}', '{researcher_id}', '{year}', '{type_}')
    """.format(
        graduate_program_id=GraduateProgram.graduate_program_id,
        researcher_id=GraduateProgram.researcher_id,
        year=GraduateProgram.year,
        type_=GraduateProgram.type_,
    )

    return sgbdSQL.execScript_db(sql)


def query_GpResearcher(ID):
    sql = """
    SELECT * FROM adm_graduate_program_researcher WHERE graduate_program_id = {filter}
""".format(
        filter=ID
    )
    return pd.DataFrame(
        sgbdSQL.consultar_db(sql),
        columns=[
            "graduate_program_id",
            "researcher_id",
            "year",
            "type_",
        ],
    )
