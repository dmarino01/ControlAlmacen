from models import Empresa
from db import db
from sqlalchemy import exc
from flask import flash

class ControllerEmpresa:

    @classmethod
    def getEmpresas(cls):
        try:
            empresas = Empresa.query.all()
            return empresas
        except Exception as e:
            print(f"Error fetching empresas: {e}")
            return []