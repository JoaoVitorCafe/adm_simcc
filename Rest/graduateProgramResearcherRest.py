from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

graduateProgramResearcherRest = Blueprint('graduateProgramResearcherRest', __name__)

@graduateProgramResearcherRest.route('/graduateProgramResearcherRest', methods=['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    return jsonify("Hello graduateProgramResearcherRest"), 200