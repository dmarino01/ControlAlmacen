from db import db

class Puerta(db.Model):
    __tablename__ = 'puertas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    estado_id = db.Column(db.Integer, db.ForeignKey('puerta_estados.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    duracion = db.Column(db.String(50))
    vencimiento = db.Column(db.Date)
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'))