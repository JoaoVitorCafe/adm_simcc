from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

researcherRest = Blueprint('researcherRest', __name__)

@researcherRest.route('/researcherRest', methods=['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    return jsonify("Hello researcherRest"), 200