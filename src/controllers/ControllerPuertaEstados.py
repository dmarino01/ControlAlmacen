from models import PuertaEstado
from db import db

class ControllerPuertaEstados:

    @classmethod
    def getPuertaEstados(cls):
        try:
            PuertaEstados = PuertaEstado.query.all()
            return PuertaEstados
        except Exception as e:
            print(f"Error fetching PuertaEstados: {e}")
            return []