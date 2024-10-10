from models import Almacen, Puerta, ContratoPuertas, Contrato
from db import db
from sqlalchemy import exc
from sqlalchemy.orm import joinedload
from flask import flash


class ControllerAlmacen:

    @classmethod
    def getAlmacenes(cls):
        try:
            almacenes = Almacen.query.options(
                joinedload(Almacen.puertas)
                .joinedload(Puerta.contrato_puertas)
                .joinedload(ContratoPuertas.contrato)
                .joinedload(Contrato.cliente)
            ).all()
            return almacenes
        except Exception as e:
            print(f"Error fetching almacenes: {e}")
            return []

    @classmethod
    def createAlmacen(cls, nombre, empresa_id):
        nuevo_almacen = Almacen(nombre=nombre, empresa_id=empresa_id)
        try:
            db.session.add(nuevo_almacen)
            db.session.commit()
            flash('¡Almacen creado exitosamente!', 'success')
            return nuevo_almacen.id
        except exc.IntegrityError:
            db.session.rollback()
            flash('Error de integridad: el almacen ya existe.', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e

    @classmethod
    def updateAlmacen(cls, id, nombre, empresa_id):
        try:
            almacen = Almacen.query.get(id)
            if not almacen:
                raise ValueError("Almacen no encontrado.")
            almacen.nombre = nombre
            almacen.empresa_id = empresa_id
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
