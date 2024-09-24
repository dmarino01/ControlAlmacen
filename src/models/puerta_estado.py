from db import db

class PuertaEstado(db.Model):
    __tablename__ = 'puerta_estados'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

    # Relationships
    puertas = db.relationship('Puerta', backref='estado', lazy=True)
