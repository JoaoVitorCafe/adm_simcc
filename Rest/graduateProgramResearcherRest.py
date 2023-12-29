from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import GraduateProgramResearcherSQL
from Model.GraduateProgramResearcher import GraduateProgramResearcher

graduateProgramResearcherRest = Blueprint("graduateProgramResearcherRest", __name__)


@graduateProgramResearcherRest.route(
    "/GraduateProgramResearcherRest/Query", methods=["GET"]
)
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonGpResearcher = list()
    dfGpResearcher = GraduateProgramResearcherSQL.query(
        request.args.get("institution_id")
    )
    for Index, GpResearcher in dfGpResearcher.iterrows():
        graduation_program_researcher_inst = GraduateProgramResearcher()
        graduation_program_researcher_inst.graduate_program_id = GpResearcher[
            "graduate_program_id"
        ]
        graduation_program_researcher_inst.researcher_id = GpResearcher["researcher_id"]
        graduation_program_researcher_inst.year = GpResearcher["year"]
        graduation_program_researcher_inst.type_ = GpResearcher["type_"]

        JsonGpResearcher.append(graduation_program_researcher_inst.get_json())

    return jsonify(JsonGpResearcher), 200


@graduateProgramResearcherRest.route(
    "/GraduateProgramResearcherRest/Insert", methods=["POST"]
)
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonGpResearcher = request.get_json()
    if not JsonGpResearcher:
        return jsonify({"error": "Erro no Json enviado"}), 400
    try:
        for GpResearcher_data in JsonGpResearcher:
            gp_researcher_inst = GraduateProgramResearcher()
            gp_researcher_inst.graduate_program_id = GpResearcher_data[
                "graduate_program_id"
            ]
            gp_researcher_inst.researcher_id = GpResearcher_data["researcher_id"]
            gp_researcher_inst.year = GpResearcher_data["year"]
            gp_researcher_inst.type_ = GpResearcher_data["type_"]

            GraduateProgramResearcherSQL.insert(gp_researcher_inst)
    except Exception as Error:
        return jsonify(f"{Error}"), 400

    return jsonify("Incerssão bem sucedida"), 200
