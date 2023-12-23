from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

graduateProgramRest = Blueprint('graduateProgramRest', __name__)

@graduateProgramRest.route('/graduateProgramRest', methods=['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    return jsonify("Hello graduateProgramRest"), 200