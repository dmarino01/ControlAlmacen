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