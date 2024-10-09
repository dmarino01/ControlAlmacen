from db import db

class Empresa(db.Model):
    __tablename__ = 'empresas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    #Relationships
    almacenes = db.relationship('Almacen', back_populates='empresa', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre