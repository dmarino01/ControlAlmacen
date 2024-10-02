from models import Almacen
from db import db
from sqlalchemy import exc
from flask import flash

class ControllerAlmacen:

    @classmethod
    def getAlmacenes(cls):
        try:
            almacenes = Almacen.query.filter_by(is_deleted=False).all()
            return almacenes
        except Exception as e:
            print(f"Error fetching almacenes: {e}")
            return []
        
    @classmethod
    def createAlmacen(cls, nombre):
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
        
    @classmethod
    def updateAlmacen(cls, id, nombre):
        try:
            almacen = Almacen.query.get(id)
            if not almacen:
                raise ValueError("Almacen no encontrado.")
            almacen.nombre = nombre
            db.session.commit()
            flash('¡Almacen actualizado exitosamente', 'success')
            return almacen
        except exc.IntegrityError:
            db.session.rollback()
            flash('Error de integridad: el almacen ya existe.', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar el almacen: {e}")
            raise e
        
    @classmethod
    def deleteAlmacen(cls, id):
        try:
            almacen = Almacen.query.get(id)
            if not almacen:
                raise ValueError("Almacen no encontrado.")
            almacen.is_deleted = True
            db.session.commit()
            flash('¡Almacen eliminado correctamente!', 'success')
            return almacen
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el almacen: {e}")
            raise e