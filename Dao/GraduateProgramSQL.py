# Para conseguir importar os modulos de projeto em tempo de execução desse script
import sys

sys.path.append("../")

import Dao.dbHandler as dbHandler
import pandas as pd
from Model.GraduateProgram import GraduateProgram


def insert(GraduateProgram):
    sql = """
    INSERT INTO graduate_program (graduate_program_id, code, name, area, modality, TYPE, rating, institution_id, description, url_image, city, visible)
    VALUES
        ('{graduate_program_id}', '{code}', '{name}', '{area}', '{modality}', '{TYPE}', '{rating}', '{institution_id}', '{description}', '{url_image}', '{city}', '{visible}')
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
        city=GraduateProgram.city,
        visible=GraduateProgram.visible,
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
            "city",
            "visible",
            "created_at",
            "updated_at",
        ],
    )


def Update(ID):
    sql = """UPDATE graduate_program SET visible = NOT visible WHERE graduate_program_id = '{filter}';""".format(
        filter=ID
    )
    dbHandler.execScript_db(sql=sql)
    return "Update concluido"


def Delete(ID):
    sql = """DELETE FROM graduate_program WHERE graduate_program_id = '{filter}';""".format(
        filter=ID
    )
    dbHandler.execScript_db(sql=sql)
    return "Delete concluido"
