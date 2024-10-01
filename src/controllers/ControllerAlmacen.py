from models import Almacen
from db import db
from sqlalchemy import exc
from flask import flash

class ControllerAlmacen:

    @classmethod
    def getAlmacenes(cls):
        try:
            almacenes = Almacen.query.all()
            return almacenes
        except Exception as e:
            print(f"Error fetching almacenes: {e}")
            return []
        
    @classmethod
    def createAlmacenes(cls, nombre):
        nuevo_almacen = Almacen(nombre=nombre)
        try:
            db.session.add(nuevo_almacen)
            db.session.commit()
            flash('¡Almacen creado exitosamente!', 'success')
            return nuevo_almacen
        except exc.IntegrityError:
            db.session.rollback()
            flash('Error de integridad: el almacen ya existe.', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e