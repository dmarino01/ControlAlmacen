from db import db
from models.Contrato import Contrato

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    contacto = db.Column(db.String(100))

    #Relationships
    contratos = db.relationship(Contrato, backref='Cliente', lazy=True)

    def __repr__(self):
        return (
            f"<Cliente id={self.id}, "
            f"nombre={self.nombre}, "
            f"contacto={self.contacto}>"
        )

