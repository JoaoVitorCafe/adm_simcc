# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.GraduateProgram import GraduateProgram


def insert(GraduateProgram):
    sql = """
    INSERT INTO graduate_program (graduate_program_id, code, name, area, modality, TYPE, rating, institution_id, description, url_image)
    VALUES
        ('{graduate_program_id}', '{code}', '{name}', '{area}', '{modality}', '{TYPE}', '{rating}', '{institution_id}', '{description}', '{url_image}')
    """.format(
        graduate_program_id=GraduateProgram.graduate_program_id,
        code=GraduateProgram.code,
        name=GraduateProgram.name,
        area=GraduateProgram.area,
        modality=GraduateProgram.modality,
        TYPE=GraduateProgram.type,
        rating=GraduateProgram.rating,
        institution_id=GraduateProgram.institution_id,
        description=GraduateProgram.description,
        url_image=GraduateProgram.url_image,
    )

    return dbHandler.execScript_db(sql)


def query(ID):
    sql = """
    SELECT * FROM graduate_program WHERE institution_id = {filter}
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
            "description",
            "url_image",
            "created_at",
            "updated_at",
        ],
    )