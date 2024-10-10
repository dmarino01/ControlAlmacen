from db import db

class ContratoPuertas(db.Model):
    __tablename__ = 'contrato_puertas'

    contrato_id = db.Column(db.Integer, db.ForeignKey('contratos.id'), nullable=False)
    puerta_id = db.Column(db.Integer, db.ForeignKey('puertas.id'), nullable=False, primary_key=True)

    # Relationships
    contrato = db.relationship('Contrato', back_populates='contrato_puertas')
    puerta = db.relationship('Puerta', back_populates='contrato_puertas')

    def __init__(self, contrato_id, puerta_id):
        self.contrato_id = contrato_id
        self.puerta_id = puerta_id