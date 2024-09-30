from db import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True)
    contacto = db.Column(db.String(100))

    #Relationships
    contratos = db.relationship('Contrato', back_populates='cliente', lazy=True)

    def __repr__(self):
        return (
            f"<Cliente id={self.id}, "
            f"nombre={self.nombre}, "
            f"contacto={self.contacto}, "
            f"contratos={self.contratos}>"
        )

