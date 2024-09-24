from db import db

class Contrato(db.Model):
    __tablename__ = 'contratos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    puerta_id = db.Column(db.Integer, db.ForeignKey('puertas.id'))
    fecha_inicio = db.Column(db.Date)
    fecha_final = db.Column(db.Date)

    cliente = db.relationship('Cliente', back_populates='contratos')
    puerta = db.relationship('Puerta', back_populates='contrato')
    
    def __repr__(self):
        return (
            f"<Contrato id={self.id}, "
            f"cliente_id={self.cliente_id}, "
            f"puerta_id={self.puerta_id}, "
            f"fecha_inicio={self.fecha_inicio}, "
            f"fecha_final={self.fecha_final}>"
        )