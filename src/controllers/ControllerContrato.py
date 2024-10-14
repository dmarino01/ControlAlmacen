from models import Contrato
from db import db
from sqlalchemy import exc
from flask import flash

class ControllerContrato:

    @classmethod
    def getContratos(cls):
        try:
            contratos = Contrato.query.filter_by(is_deleted=False).all()
            return contratos
        except Exception as e:
            print(f"Error fetching contratos: {e}")
            return []
        
    @classmethod
    def createContrato(cls, cliente_id, renta, fecha_inicio, fecha_final):
        nuevo_contrato = Contrato(cliente_id=cliente_id, renta=renta, fecha_inicio=fecha_inicio, fecha_final=fecha_final)
        try:
            db.session.add(nuevo_contrato)
            db.session.commit()
            flash('Contrato creado exitosamente!', 'success')
            return nuevo_contrato.id
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        
    @classmethod
    def deleteContrato(cls, id):
        try:
            contrato = Contrato.query.get(id)
            if not contrato:
                raise ValueError("Contrato no encontrado.")
            contrato.is_deleted = True
            db.session.commit()
            flash('¡Contrato eliminado correctamente!', 'success')
            return contrato
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el contrato: {e}")
            raise e