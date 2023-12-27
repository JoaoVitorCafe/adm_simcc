from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import dbHandler as db

graduateProgramResearcherRest = Blueprint("graduateProgramResearcherRest", __name__)


@graduateProgramResearcherRest.route("/graduateProgramResearcherRest", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    
    JsonGraduateProgramsResearcher = request.get_json()

    if not JsonGraduateProgramsResearcher:
        return jsonify({"error": "Erro no Json enviado"}), 400

    str_values = str()
    for GraduatePrograms in JsonGraduateProgramsResearcher:
        str_values += f"('{GraduatePrograms["graduate_program_id"]}', '{GraduatePrograms["researcher_id"]}','{GraduatePrograms["year"]}','{GraduatePrograms["type_"]}'),"

    db.execScript_db(f"INSERT INTO adm_graduate_program_researcher (graduate_program_id, researcher_id, year, type_) values {str_values[:-1]}")

    return jsonify("Hello graduateProgramResearcherRest"), 200
