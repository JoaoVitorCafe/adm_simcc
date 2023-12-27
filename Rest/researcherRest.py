from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import ResearcherSQL
from Model.Resercher import Researcher

researcherRest = Blueprint("researcherRest", __name__)


@researcherRest.route("/admResearcher/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonIDs = request.get_json()
    if not JsonIDs:
        return jsonify({"error": "Erro no Json enviado"}), 400

    JsonResearchers = list()
    for ID in JsonIDs:
        dfResearcher = ResearcherSQL.query_researcher(int(ID["institution_id"]))

        for Index, researcher in dfResearcher.iterrows():
            Rs = Researcher()
            Rs.researcher_id = researcher.researcher_id
            Rs.name = researcher.name
            Rs.lattes_id = researcher.lattes_id
            Rs.institution_id = researcher.institution_id

            JsonResearchers.append(Rs.get_json())

    return jsonify(JsonResearchers), 200


@researcherRest.route("/admResearcher/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    # Nota - Melhorar a forma de instanciar
    for researcher_data in JsonInstitutions:
        Rs = Researcher()
        Rs.researcher_id = researcher_data["researcher_id"]
        Rs.name = researcher_data["name"]
        Rs.lattes_id = researcher_data["lattes_id"]
        Rs.institution_id = researcher_data["institution_id"]

        ResearcherSQL.insert_researcher(Rs)

    return jsonify("Hello institutionRest"), 200
