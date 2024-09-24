from db import db
from models.Contrato import Contrato

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    contacto = db.Column(db.String(100))

    #Relationships
    contratos = db.relationship(Contrato, backref='Cliente', lazy=True)

