from db import db
from models.Contrato import Contrato

class Puerta(db.Model):
    __tablename__ = 'puertas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    estado_id = db.Column(db.Integer, db.ForeignKey('puerta_estados.id'))
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'))

    #Relationships
    contratos = db.relationship(Contrato, backref='Puerta', lazy=True)
