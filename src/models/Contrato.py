from db import db

class Contrato(db.Model):
    __tablename__ = 'contratos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    renta = db.Column(db.Float, nullable=True)
    fecha_inicio = db.Column(db.Date)
    fecha_final = db.Column(db.Date)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    cliente = db.relationship('Cliente', back_populates='contratos', lazy=True)
    contrato_puertas = db.relationship('ContratoPuertas', back_populates='contrato')

    def __init__(self, cliente_id, renta, fecha_inicio, fecha_final, is_deleted=False):
        self.cliente_id = cliente_id
        self.renta = renta
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.is_deleted = is_deleted
    
    def __repr__(self):
        return (
            f"<Contrato id={self.id}, "
            f"cliente_id={self.cliente_id}, "
            f"renta={self.renta}, "
            f"fecha_inicio={self.fecha_inicio}, "
            f"fecha_final={self.fecha_final}>"
        )