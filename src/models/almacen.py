from db import db
from models.Almacen_css_detalles import AlmacenCSSDetalles
from models.Puerta import Puerta

class Almacen(db.Model):
    __tablename__ = 'almacenes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    #Relationships
    almacen_css_detalles = db.relationship(AlmacenCSSDetalles, backref='Almacen', lazy=True)
    puertas = db.relationship(Puerta, backref='Almacen', lazy=True)

    def __repr__(self):
        return (
            f"<Almacen id={self.id}, "
            f"nombre={self.nombre}, "
            f"puertas={self.puertas}>"
        )