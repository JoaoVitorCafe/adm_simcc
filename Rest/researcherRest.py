from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import dbHandler as db
researcherRest = Blueprint("researcherRest", __name__)


@researcherRest.route("/researcherRest", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def route():

    JsonResearchers = request.get_json()

    if not JsonResearchers:
        return jsonify({"error": "Erro no Json enviado"}), 400

    str_values = str()
    for researcher in JsonResearchers:
        str_values += f"('{researcher["researcher_id"]}', '{researcher["name"]}', '{researcher["lattes_id"]}', '{researcher["institution_id"]}'),"

    db.execScript_db(f"INSERT INTO adm_researcher (researcher_id, name, lattes_id, institution_id) values {str_values[:-1]}")

    return jsonify("Hello researcherRest"), 200
