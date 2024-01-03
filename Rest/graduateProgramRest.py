from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

from Dao import GraduateProgramSQL
from Model.GraduateProgram import GraduateProgram

graduateProgramRest = Blueprint("graduateProgramRest", __name__)


@graduateProgramRest.route("/GraduateProgramRest/Query", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type"])
def Query():
    JsonGraduateProgram = list()
    dfGraduateProgram = GraduateProgramSQL.Query(request.args.get("institution_id"))

    for Index, graduateprogram in dfGraduateProgram.iterrows():
        graduation_program_inst = GraduateProgram()
        graduation_program_inst.graduate_program_id = graduateprogram[
            "graduate_program_id"
        ]
        graduation_program_inst.code = graduateprogram["code"]
        graduation_program_inst.name = graduateprogram["name"]
        graduation_program_inst.area = graduateprogram["area"]
        graduation_program_inst.modality = graduateprogram["modality"]
        graduation_program_inst.type = graduateprogram["type"]
        graduation_program_inst.rating = graduateprogram["rating"]
        graduation_program_inst.institution_id = graduateprogram["institution_id"]
        graduation_program_inst.description = graduateprogram["description"]
        graduation_program_inst.url_image = graduateprogram["url_image"]
        graduation_program_inst.city = graduateprogram["city"]
        graduation_program_inst.visible = graduateprogram["visible"]

        JsonGraduateProgram.append(graduation_program_inst.get_json())

    return jsonify(JsonGraduateProgram), 200


@graduateProgramRest.route("/GraduateProgramRest/Update", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Update():
    GraduateProgramSQL.Update(request.args.get("graduate_program_id"))
    return jsonify("Update bem sucedido"), 200


@graduateProgramRest.route("/GraduateProgramRest/Insert", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Insert():
    JsonGraduateProgram = request.get_json()

    if not JsonGraduateProgram:
        return jsonify({"error": "Erro no Json enviado"}), 400

    for GraduateProgram_data in JsonGraduateProgram:
        try:
            graduation_program_inst = GraduateProgram()
            graduation_program_inst.graduate_program_id = GraduateProgram_data[
                "graduate_program_id"
            ]
            graduation_program_inst.code = GraduateProgram_data["code"]
            graduation_program_inst.name = GraduateProgram_data["name"]
            graduation_program_inst.area = GraduateProgram_data["area"]
            graduation_program_inst.modality = GraduateProgram_data["modality"]
            graduation_program_inst.type = GraduateProgram_data["type"]
            graduation_program_inst.rating = GraduateProgram_data["rating"]
            graduation_program_inst.institution_id = GraduateProgram_data[
                "institution_id"
            ]
            graduation_program_inst.description = GraduateProgram_data["description"]
            graduation_program_inst.url_image = GraduateProgram_data["url_image"]
            graduation_program_inst.city = GraduateProgram_data["city"]
            graduation_program_inst.visible = GraduateProgram_data["visible"]

            GraduateProgramSQL.Insert(graduation_program_inst)
        except Exception as Error:
            return jsonify(f"{Error}"), 400

    return jsonify("OK"), 200


@graduateProgramRest.route("/GraduateProgramRest/Delete", methods=["DELETE"])
@cross_origin(origin="*", headers=["Content-Type"])
def Delete():
    GraduateProgramSQL.Delete(request.args.get("graduate_program_id"))
    return jsonify("Ok"), 200


@graduateProgramRest.route("/GraduateProgramRest/Fix", methods=["POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def Fix():
    JsonGraduateProgram = request.get_json()

    if not JsonGraduateProgram:
        return jsonify({"error": "Erro no Json enviado"}), 400

    for GraduateProgram_data in JsonGraduateProgram:
        try:
            graduation_program_inst = GraduateProgram()
            graduation_program_inst.graduate_program_id = GraduateProgram_data[
                "graduate_program_id"
            ]
            graduation_program_inst.code = GraduateProgram_data["code"]
            graduation_program_inst.name = GraduateProgram_data["name"]
            graduation_program_inst.area = GraduateProgram_data["area"]
            graduation_program_inst.modality = GraduateProgram_data["modality"]
            graduation_program_inst.type = GraduateProgram_data["type"]
            graduation_program_inst.rating = GraduateProgram_data["rating"]
            graduation_program_inst.institution_id = GraduateProgram_data[
                "institution_id"
            ]
            graduation_program_inst.description = GraduateProgram_data["description"]
            graduation_program_inst.url_image = GraduateProgram_data["url_image"]
            graduation_program_inst.city = GraduateProgram_data["city"]
            graduation_program_inst.visible = GraduateProgram_data["visible"]

            GraduateProgramSQL.Fix(graduation_program_inst)
        except Exception as Error:
            return jsonify(f"{Error}"), 400

    return jsonify("OK"), 200
