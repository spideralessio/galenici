from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app.db'


db = SQLAlchemy(app)



api = Api(app)

# Diagnosis
# shows a single diagnosis item
class Diagnosis(Resource):
	def get(self, diagnosis_id):
		return models.Diagnosis.query.get(1)

# DiagnosisList
# shows a list of diagnosis
class DiagnosisList(Resource):
	def get(self):
		return models.Diagnosis.query.all()


# Drug
# shows a single drug item
class Drug(Resource):
	def get(self, drug_id):
		return {"N":models.Drug.query.get(1).recipe}


# DrugList
# shows a list of drugs
class DrugList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		#self.reqparse.add_argument('pippo', type=str, required=True, help="No task title provided")
		self.args = self.reqparse.parse_args()
	def get(self):
		print(self.args)
		return models.Drug.query.all()
	


##
## Actually setup the Api resource routing here
##
api.add_resource(DrugList, '/drugs')
api.add_resource(Drug, '/drugs/<drug_id>')


if __name__ == '__main__':
	app.run(debug=True)