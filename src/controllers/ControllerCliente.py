from models import Cliente
from db import db
from sqlalchemy import exc
class ControllerCliente:

    @classmethod
    def getClientes(cls):
        try:
            clientes = Cliente.query.all()
            return clientes
        except Exception as e:
            print(f"Error fetching clientes: {e}")
            return []
        
    @classmethod
    def createCliente(cls, nombre, contacto):
        nuevo_cliente = Cliente(nombre=nombre, contacto=contacto)
        try:
            db.session.add(nuevo_cliente)
            db.session.commit()
            return nuevo_cliente
        except exc.IntegrityError:
            db.session.rollback()
            print(f"Integrity error: {e}")
            raise ValueError("El cliente ya existe")
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        
    @classmethod
    def updateCliente(cls, nombre, contacto, id):
        try:
            cliente = Cliente.query.get(id)
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            cliente.nombre = nombre
            cliente.contacto = contacto
            db.session.commit()
            return
        except Exception as e:
            db.session.rollback()
            print(f"Error al actualizar el cliente: {e}")
            raise e
