from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import ResearcherSQL
from Model.Resercher import Researcher

researcherRest = Blueprint("researcherRest", __name__)


@researcherRest.route("/Researcher/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonResearchers = list()

    dfResearcher = ResearcherSQL.query(request.args.get("institution_id"))

    for Index, researcher in dfResearcher.iterrows():
        researcher_inst = Researcher()
        researcher_inst.researcher_id = researcher["researcher_id"]
        researcher_inst.name = researcher["name"]
        researcher_inst.lattes_id = researcher["lattes_id"]
        researcher_inst.institution_id = researcher["institution_id"]

        JsonResearchers.append(researcher_inst.get_json())

    return jsonify(JsonResearchers), 200


@researcherRest.route("/Researcher/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonInstitutions = request.get_json()

    if not JsonInstitutions:
        return jsonify({"error": "Erro no Json enviado"}), 400

    try:
        for researcher_data in JsonInstitutions:
            researcher_inst = Researcher()
            researcher_inst.researcher_id = researcher_data["researcher_id"]
            researcher_inst.name = researcher_data["name"]
            researcher_inst.lattes_id = researcher_data["lattes_id"]
            researcher_inst.institution_id = researcher_data["institution_id"]

            ResearcherSQL.insert(researcher_inst)
    except Exception as Error:
        return jsonify(f"{Error}"), 400

    return jsonify("Incerssão bem sucedida"), 200
