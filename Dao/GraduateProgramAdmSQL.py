# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.GraduateProgramAdm import GraduateProgram


def insert_graduationProgram(GraduateProgram):
    sql = """
    INSERT INTO adm_graduate_program (graduate_program_id, code, name, area, modality, TYPE, rating, institution_id)
    VALUES
        ('{graduate_program_id}', '{code}', '{name}', '{area}', '{modality}', '{TYPE}', '{rating}', '{institution_id}')
    """.format(
        graduate_program_id=GraduateProgram.graduate_program_id,
        code=GraduateProgram.code,
        name=GraduateProgram.name,
        area=GraduateProgram.area,
        modality=GraduateProgram.modality,
        TYPE=GraduateProgram.type,
        rating=GraduateProgram.rating,
        institution_id=GraduateProgram.institution_id,
    )

    return dbHandler.execScript_db(sql)


def query_graduateProgram(ID):
    sql = """
    SELECT * FROM adm_graduate_program WHERE institution_id = {filter}
""".format(
        filter=ID
    )
    return pd.DataFrame(
        dbHandler.consultar_db(sql),
        columns=[
            "graduate_program_id",
            "code",
            "name",
            "area",
            "modality",
            "type",
            "rating",
            "institution_id",
        ],
    )
