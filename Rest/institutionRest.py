from flask import jsonify, request, Blueprint
from flask_cors import cross_origin

institutionRest = Blueprint('institutionRest', __name__)

@institutionRest.route('/institutionRest', methods=['GET'])
@cross_origin(origin="*", headers=["Content-Type"])
def route():
    return jsonify("Hello institutionRest"), 200