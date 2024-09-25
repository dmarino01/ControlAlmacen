from db import db

class Almacen(db.Model):
    __tablename__ = 'almacenes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    #Relationships
    almacenCSSDetalles = db.relationship('AlmacenCSSDetalles', back_populates='almacen', lazy=True)
    puertas = db.relationship('Puerta', back_populates='almacen', lazy=True)

    def __repr__(self):
        return (
            f"<Almacen id={self.id}, "
            f"nombre={self.nombre}, "
            f"detalles={self.almacenCSSDetalles}>"
            f"puertas={self.puertas}>"
        )