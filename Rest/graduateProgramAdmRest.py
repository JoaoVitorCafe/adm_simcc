from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import GraduateProgramAdmSQL
from Model.GraduateProgramAdm import GraduateProgram

graduateProgramAdmRest = Blueprint("graduateProgramAdmRest", __name__)


@graduateProgramAdmRest.route("/admGraduateProgramRest/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonIDs = request.get_json()
    if not JsonIDs:
        return jsonify({"error": "Erro no Json enviado"}), 400

    JsonGraduateProgram = list()
    for ID in JsonIDs:
        dfGraduateProgram = GraduateProgramAdmSQL.query_graduateProgram(
            int(ID["institution_id"])
        )

        for Index, graduateprogram in dfGraduateProgram.iterrows():
            Gp = GraduateProgram()
            Gp.graduate_program_id = graduateprogram.graduate_program_id
            Gp.code = graduateprogram.code
            Gp.name = graduateprogram.name
            Gp.area = graduateprogram.area
            Gp.modality = graduateprogram.modality
            Gp.type = graduateprogram.type
            Gp.rating = graduateprogram.rating
            Gp.institution_id = graduateprogram.institution_id

            JsonGraduateProgram.append(Gp.get_json())

    return jsonify(JsonGraduateProgram), 200


@graduateProgramAdmRest.route("/admGraduateProgramRest/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonGraduateProgram = request.get_json()

    if not JsonGraduateProgram:
        return jsonify({"error": "Erro no Json enviado"}), 400

    for GraduateProgram_data in JsonGraduateProgram:
        Gp = GraduateProgram()
        Gp.graduate_program_id = GraduateProgram_data["graduate_program_id"]
        Gp.code = GraduateProgram_data["code"]
        Gp.name = GraduateProgram_data["name"]
        Gp.area = GraduateProgram_data["area"]
        Gp.modality = GraduateProgram_data["modality"]
        Gp.type = GraduateProgram_data["type"]
        Gp.rating = GraduateProgram_data["rating"]
        Gp.institution_id = GraduateProgram_data["institution_id"]

        GraduateProgramAdmSQL.insert_graduationProgram(Gp)

    return jsonify("Hello graduateProgramAdmRest"), 200
