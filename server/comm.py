from app import db
from models import *

#db.create_all()
'''
diagnosis = Diagnosis("TIROIDE")
drug = Drug()
drug.recipe = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
drug.diagnosis.append(diagnosis)
db.session.add(drug)
db.session.commit()'''

drugs = Diagnosis.query.all()
print(drugs)