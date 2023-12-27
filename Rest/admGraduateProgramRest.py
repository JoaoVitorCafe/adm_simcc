from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import dbHandler as db

admGraduateProgramRest = Blueprint('admGraduateProgramRest', __name__)

@graduateProgramRest.route('/graduateProgramRest', methods=['POST'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    
    JsonGraduatePrograms = request.get_json()

    if not JsonGraduatePrograms:
        return jsonify({"error": "Erro no Json enviado"}), 400

    str_values = str()
    for GraduatePrograms in JsonGraduatePrograms:
        str_values += f"('{GraduatePrograms["graduate_program_id"]}', '{GraduatePrograms["code"]}', '{GraduatePrograms["area"]}', '{GraduatePrograms["modality"]}', '{GraduatePrograms["TYPE"]}','{GraduatePrograms["rating"]}','{GraduatePrograms["institution_id"]}'),"

    db.execScript_db(f"INSERT INTO adm_graduate_program (graduate_program_id, code, area, modality, TYPE, rating, institution_id) values {str_values[:-1]}")

    return jsonify("Hello graduateProgramRest"), 200
