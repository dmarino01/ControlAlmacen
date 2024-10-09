from db import db

class Almacen(db.Model):
    __tablename__ = 'almacenes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'), nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    #Relationships
    empresa = db.relationship('Empresa', back_populates='almacenes', lazy=True, uselist=False)
    almacenCSSDetalles = db.relationship('AlmacenCSSDetalles', back_populates='almacen', lazy=True)
    puertas = db.relationship('Puerta', back_populates='almacen')

    def __init__(self, nombre, empresa_id, is_deleted=False):
        self.nombre = nombre
        self.empresa_id = empresa_id
        self.is_deleted = is_deleted

    def __repr__(self):
        return (
            f"<Almacen id={self.id}, "
            f"nombre={self.nombre}, "
            f"nombre={self.empresa_id}, "
            f"detalles={self.almacenCSSDetalles}, "
            f"puertas={self.puertas}>"
        )
    
    @property
    def numero_de_puertas(self):
        return len(self.puertas)