from db import db

class Contrato(db.Model):
    __tablename__ = 'contratos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    puerta_id = db.Column(db.Integer, db.ForeignKey('puertas.id'))
    fecha_inicio = db.Column(db.Date)
    fecha_final = db.Column(db.Date)