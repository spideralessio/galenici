from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

drug_diagnosis_table = db.Table('drug_diagnosis_table',
    db.Column('drug_id', db.Integer, db.ForeignKey('drug.pk')),
    db.Column('diagnosis_id', db.Integer, db.ForeignKey('diagnosis.pk'))
)

class Diagnosis(db.Model):
	__tablename__ = 'diagnosis'
	pk = Column(db.Integer, primary_key=True)
	name = Column(db.Text, unique=True)
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Diagnosis %d>' % self.pk

class Drug(db.Model):
	__tablename__ = 'drug'
	pk = Column(db.Integer, primary_key=True)
	recipe = Column(db.Text, unique=True)
	diagnosis = relationship("Diagnosis", secondary=drug_diagnosis_table)

	def __repr__(self):
		return '<Drug %d>' % self.pk