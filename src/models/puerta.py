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

    def __repr__(self):
        return (
            f"<Puerta id={self.id}, "
            f"nombre={self.nombre}, "
            f"estado_id={self.estado_id}, "
            f"almacen_id={self.almacen_id}>"
        )
