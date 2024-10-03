from models import Puerta
from db import db

class ControllerPuerta:
    
    @classmethod
    def createPuertas(cls, almacen_id, puertas_data, estado_puertas):
        try:
            for nombre_puerta, estado_puerta in zip(puertas_data, estado_puertas):
                nueva_puerta = Puerta(nombre=nombre_puerta, estado_id=estado_puerta, almacen_id=almacen_id)
                db.session.add(nueva_puerta)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        
    @classmethod
    def getPuertasPorAlmacen(cls, id):
        try:
            puertas = Puerta.query.filter_by(almacen_id=id).all()
            return puertas
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        
