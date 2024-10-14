from models import Cliente
from db import db
from sqlalchemy import exc
from flask import flash


class ControllerCliente:

    @classmethod
    def getClientes(cls):
        try:
            clientes = Cliente.query.filter_by(is_deleted=False).all()
            return clientes
        except Exception as e:
            print(f"Error fetching clientes: {e}")
            return []

    @classmethod
    def createCliente(cls, nombre, contacto, logo):
        nuevo_cliente = Cliente(nombre=nombre, contacto=contacto, logo=logo)
        try:
            db.session.add(nuevo_cliente)
            db.session.commit()
            flash('¡Cliente creado exitosamente!', 'success')
            return nuevo_cliente
        except exc.IntegrityError:
            db.session.rollback()
            flash('Error de integridad: el cliente ya existe.', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e

    @classmethod
    def updateCliente(cls, id, nombre, contacto, logo):
        try:
            cliente = Cliente.query.get(id)
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            cliente.nombre = nombre
            cliente.contacto = contacto
            if logo:
                cliente.logo = logo
            db.session.commit()
            flash('¡Cliente actualizado correctamente!', 'success')
            return cliente
        except exc.IntegrityError:
            db.session.rollback()
            flash('Error de integridad: el cliente ya existe.', 'error')
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar el cliente: {e}")
            raise e

    @classmethod
    def deleteCliente(cls, id):
        try:
            cliente = Cliente.query.get(id)
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            cliente.is_deleted = True
            db.session.commit()
            flash('¡Cliente eliminado correctamente!', 'success')
            return cliente
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el cliente: {e}")
            raise e

    @classmethod
    def removeLogo(cls, id):
        try:
            cliente = Cliente.query.get(id)
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            cliente.logo = None
            db.session.commit()
            flash('Logo eliminado correctamente!', 'success')
            return cliente
        except Exception as e:
            db.session.rollback()
            print(f"Error al eliminar el logo: {e}")
            raise e
