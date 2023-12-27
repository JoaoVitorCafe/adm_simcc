from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import dbHandler as db

institutionRest = Blueprint('institutionRest', __name__)

@institutionRest.route('/institutionRest', methods=['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    str_values = str()
    for Institution in JsonInstitutions:
        str_values += f"('{Institution["institution_id"]}', '{Institution["name"]}', '{Institution["acronym"]}', '{Institution["email_user"]}', '{Institution["PASSWORD"]}'),"

    db.execScript_db(f"INSERT INTO adm_institution (institution_id, name, acronym, email_user, PASSWORD) values {str_values[:-1]}")

    return jsonify("Hello institutionRest"), 200
