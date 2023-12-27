from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import InstitutionSQL
from Model.Institution import Institution

institutionRest = Blueprint("institutionRest", __name__)


@institutionRest.route("/admInstitution/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonIDs = request.get_json()
    if not JsonIDs:
        return jsonify({"error": "Erro no Json enviado"}), 400

    JsonInstitutions = list()
    for ID in JsonIDs:
        dfInstitutions = InstitutionSQL.query_institution(int(ID["institution_id"]))

        for Index, institution in dfInstitutions.iterrows():
            Is = Institution()
            Is.institution_id = institution.institution_id
            Is.name = institution.name
            Is.acronym = institution.acronym
            Is.email_user = institution.email_user
            Is.password = institution.password

            JsonInstitutions.append(Is.get_json())

    return jsonify(JsonInstitutions), 200


@institutionRest.route("/admInstitution/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    # Nota - Melhorar a forma de instanciar
    for institution_data in JsonInstitutions:
        institution_instance = Institution()
        institution_instance.name = institution_data["name"]
        institution_instance.acronym = institution_data["acronym"]
        institution_instance.email_user = institution_data["email_user"]
        institution_instance.password = institution_data["password"]

        InstitutionSQL.insert_institution(institution_instance)

    return jsonify("Hello institutionRest"), 200
