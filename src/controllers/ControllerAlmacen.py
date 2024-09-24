from models.Almacen import Almacen
from sqlalchemy.orm import joinedload

class ControllerAlmacen:

    @classmethod
    def getAlmacenes(cls):
        try:
            almacenes = Almacen.query.all()
            return almacenes
        except Exception as e:
            print(f"Error fetching almacenes: {e}")
            return []
