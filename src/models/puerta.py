from db import db

class Puerta(db.Model):
    __tablename__ = 'puertas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    estado_id = db.Column(db.Integer, db.ForeignKey('puerta_estados.id'))
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'))

    #Relationships
    estado = db.relationship('PuertaEstado', back_populates='puertas') 
    contrato_puertas = db.relationship('ContratoPuertas', back_populates='puerta')
    almacen = db.relationship('Almacen', back_populates='puertas', lazy=True)

    def __init__(self, nombre, almacen_id, estado_id=1):
        self.nombre = nombre
        self.estado_id = estado_id
        self.almacen_id = almacen_id

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'estado_id': self.estado_id,
            'almacen_id': self.almacen_id
        }

    def __repr__(self):
        return (
            f"<Puerta id={self.id}, "
            f"nombre={self.nombre}, "
            f"estado_id={self.estado_id}, "
            f"almacen_id={self.almacen_id}>"
        )
