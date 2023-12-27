from flask import Flask, jsonify
from Rest.graduateProgramResearcherRest import graduateProgramResearcherRest
from Rest.institutionRest import institutionRest
from Rest.researcherRest import researcherRest
from Rest.admGraduateProgramRest import admGraduateProgramRest


app = Flask(__name__)
app.register_blueprint(institutionRest)
app.register_blueprint(researcherRest)
app.register_blueprint(admGraduateProgramRest)
app.register_blueprint(graduateProgramResearcherRest)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify("Hello World"), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
