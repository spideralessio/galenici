from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import models
from flask_cors import CORS, cross_origin


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./app.db'


db = SQLAlchemy(app)



api = Api(app)

# Diagnosis
# shows a single diagnosis item
class Diagnosis(Resource):
	def get(self, diagnosis_id):
		return row2dict(models.Diagnosis.query.get(diagnosis_id))

# DiagnosisList
# shows a list of diagnosis
class DiagnosisList(Resource):
	def get(self):
		return [row2dict(a) for a in models.Diagnosis.query.all()]


# Drug
# shows a single drug item
class Drug(Resource):
	def get(self, drug_id):
		return row2dict(models.Drug.query.get(drug_id))


# DrugList
# shows a list of drugs
class DrugList(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		#self.reqparse.add_argument('pippo', type=str, required=True, help="No task title provided")
		self.args = self.reqparse.parse_args()
	def get(self):
		print(self.args)
		return [row2dict(a) for a in models.Drug.query.all()]
	

class Load(Resource):
	def get(self):
		#db.create_all()
		for d in ["PIPPO", "TEST", "MA CHE NE SO", "CUORE MATTO"]:

			diagnosis = models.Diagnosis(d)
			db.session.add(diagnosis)
		db.session.commit()
		return True
##
## Actually setup the Api resource routing here
##
api.add_resource(DrugList, '/drugs')
api.add_resource(Load, '/load')
api.add_resource(Drug, '/drugs/<drug_id>')
api.add_resource(DiagnosisList, '/diagnosis')
api.add_resource(Diagnosis, '/diagnosis/<diagnosis_id>')


if __name__ == '__main__':
	app.run(debug=True)