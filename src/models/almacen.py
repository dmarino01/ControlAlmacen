from db import db

class Almacen(db.Model):
    __tablename__ = 'almacenes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    # Relationships
    puertas = db.relationship('Puerta', backref='almacen', lazy=True)