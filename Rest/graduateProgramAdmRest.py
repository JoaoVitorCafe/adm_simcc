from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import GraduateProgramAdmSQL
from Model.GraduateProgramAdm import GraduateProgram

graduateProgramAdmRest = Blueprint("graduateProgramAdmRest", __name__)


@graduateProgramAdmRest.route("/admGraduateProgramRest/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonGraduateProgram = list()
    dfGraduateProgram = GraduateProgramAdmSQL.query(request.args.get("institution_id"))

    for Index, graduateprogram in dfGraduateProgram.iterrows():
        graduation_program_int = GraduateProgram()
        graduation_program_int.graduate_program_id = graduateprogram[
            "graduate_program_id"
        ]
        graduation_program_int.code = graduateprogram["code"]
        graduation_program_int.name = graduateprogram["name"]
        graduation_program_int.area = graduateprogram["area"]
        graduation_program_int.modality = graduateprogram["modality"]
        graduation_program_int.type = graduateprogram["type"]
        graduation_program_int.rating = graduateprogram["rating"]
        graduation_program_int.institution_id = graduateprogram["institution_id"]

        JsonGraduateProgram.append(graduation_program_int.get_json())

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

        GraduateProgramAdmSQL.insert(Gp)

    return jsonify("Hello graduateProgramAdmRest"), 200
