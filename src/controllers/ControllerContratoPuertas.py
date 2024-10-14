from models import ContratoPuertas
from db import db

class ControllerContratoPuertas:

    @classmethod
    def createContratoPuertas(cls, contrato_id, puerta_id):
        try:
            nuevo_contrato_puertas = ContratoPuertas(contrato_id=contrato_id, puerta_id=puerta_id)
            db.session.add(nuevo_contrato_puertas)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e