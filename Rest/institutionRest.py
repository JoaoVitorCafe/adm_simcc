from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import InstitutionSQL
from Model.Institution import Institution

institutionRest = Blueprint("institutionRest", __name__)


@institutionRest.route("/InstitutionRest/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonInstitutions = list()
    dfInstitutions = InstitutionSQL.query(request.args.get("institution_id"))
    for Index, institution in dfInstitutions.iterrows():
        institution_inst = Institution()
        institution_inst.institution_id = institution["institution_id"]
        institution_inst.name = institution["name"]
        institution_inst.acronym = institution["acronym"]
        institution_inst.email_user = institution["email_user"]
        institution_inst.password = institution["password"]

        JsonInstitutions.append(institution_inst.get_json())

    return jsonify(JsonInstitutions), 200


@institutionRest.route("/InstitutionRest/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    try:
        for institution_data in JsonInstitutions:
            institution_instance = Institution()
            institution_instance.institution_id = institution_data["institution_id"]
            institution_instance.name = institution_data["name"]
            institution_instance.acronym = institution_data["acronym"]
            institution_instance.email_user = institution_data["email_user"]
            institution_instance.password = institution_data["password"]

            InstitutionSQL.insert(institution_instance)
    except Exception as Error:
        return jsonify(f"{Error}"), 400

    return jsonify("Insert bem sucedido"), 200
