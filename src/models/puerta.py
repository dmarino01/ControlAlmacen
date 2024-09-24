from db import db

class Puerta(db.Model):
    __tablename__ = 'puertas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    estado_id = db.Column(db.Integer, db.ForeignKey('puerta_estados.id'))
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'))

    #Relationships
    estado = db.relationship('PuertaEstado', back_populates='puertas') 
    contrato = db.relationship('Contrato', back_populates='puerta', lazy=True, uselist=False)

    def __repr__(self):
        return (
            f"<Puerta id={self.id}, "
            f"nombre={self.nombre}, "
            f"estado_id={self.estado_id}, "
            f"almacen_id={self.almacen_id},"
            f"contrato={self.contrato}>"
        )
