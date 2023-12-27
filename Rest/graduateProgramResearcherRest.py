from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import GraduateProgramResearcherSQL
from Model.GraduateProgramResearcher import GraduateProgramResearcher

graduateProgramResearcherRest = Blueprint("graduateProgramResearcherRest", __name__)


@graduateProgramResearcherRest.route(
    "/admGraduateProgramResearcherRest/Query", methods=["GET"]
)
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonIDs = request.get_json()
    if not JsonIDs:
        return jsonify({"error": "Erro no Json enviado"}), 400

    JsonGpResearcher = list()
    for ID in JsonIDs:
        dfGpResearcher = GraduateProgramResearcherSQL.query_GpResearcher(
            int(ID["graduate_program_id"])
        )
        for Index, GpResearcher in dfGpResearcher.iterrows():
            GpR = GraduateProgramResearcher()
            GpR.graduate_program_id = GpResearcher.graduate_program_id
            GpR.researcher_id = GpResearcher.researcher_id
            GpR.year = GpResearcher.year
            GpR.type_ = GpResearcher.type_

            JsonGpResearcher.append(GpR.get_json())

    return jsonify(JsonGpResearcher), 200


@graduateProgramResearcherRest.route(
    "/admGraduateProgramResearcherRest/Insert", methods=["POST"]
)
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonGpResearcher = request.get_json()
    if not JsonGpResearcher:
        return jsonify({"error": "Erro no Json enviado"}), 400

    for GpResearcher_data in JsonGpResearcher:
        GpR = GraduateProgramResearcher()
        GpR.graduate_program_id = GpResearcher_data["graduate_program_id"]
        GpR.researcher_id = GpResearcher_data["researcher_id"]
        GpR.year = GpResearcher_data["year"]
        GpR.type_ = GpResearcher_data["type_"]

        GraduateProgramResearcherSQL.insert_GpResearcher(GpR)

    return jsonify("Hello graduateProgramResearcherRest"), 200
