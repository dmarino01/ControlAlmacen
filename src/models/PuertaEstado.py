from db import db

class PuertaEstado(db.Model):
    __tablename__ = 'puerta_estados'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

    #Relationships
    puertas = db.relationship('Puerta', back_populates='estado', lazy=True)

    def __repr__(self):
        return (
            f"<PuertaEstado id={self.id}, "
            f"descripcion={self.descripcion}>"
        )
