from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import dbHandler as db

institutionRest = Blueprint('institutionRest', __name__)


# Imagino que a senha não deva ser passada por aqui, mas mantive, seguindo o SQL que Eduardo enviou
@institutionRest.route('/institutionRest', methods=['POST'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    
    """Comando para teste:

        curl -X POST -H "Content-Type: application/json" -d '[
    {
      "institution_id": 1,
      "name": "Universidade ABC",
      "acronym": "UABC",
      "email_user": "uabc@example.com",
      "password": "senha123"
    },
    {
      "institution_id": 2,
      "name": "Instituto XYZ",
      "acronym": "IXYZ",
      "email_user": "ixyz@example.com",
      "password": "senha456"
    },
    {
      "institution_id": 3,
      "name": "Faculdade 123",
      "acronym": "F123",
      "email_user": "f123@example.com",
      "password": "senha789"
    }
]' http://127.0.0.1:5000/institutionRest

    Returns:
        JSON: "Hello institutionRest"
    """
    
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    str_values = str()
    for Institution in JsonInstitutions:
        str_values += f"('{Institution["institution_id"]}', '{Institution["name"]}', '{Institution["acronym"]}', '{Institution["email_user"]}', '{Institution["password"]}'),"

    db.execScript_db(f"INSERT INTO adm_institution (institution_id, name, acronym, email_user, PASSWORD) values {str_values[:-1]}")

    return jsonify("Hello institutionRest"), 200
