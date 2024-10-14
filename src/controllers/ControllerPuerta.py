from models import Puerta, Almacen
from flask import jsonify
from db import db


class ControllerPuerta:

    @classmethod
    def createPuertas(cls, nombre, almacen_id):
        try:   
            nueva_puerta = Puerta(nombre=nombre, almacen_id=almacen_id)
            db.session.add(nueva_puerta)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        

    @classmethod
    def getPuertaPorId(cls, id):
        try:
            puertas = Puerta.query.get(id)
            return puertas
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
        

    @classmethod
    def getPuertasPorAlmacen(cls, almacen_id, estado_id=None):
        try:
            if estado_id is None:
                puertas = Puerta.query.filter_by(almacen_id=almacen_id).all()
            else:
                puertas = Puerta.query.filter_by(
                    almacen_id=almacen_id, estado_id=estado_id).all()
            return puertas
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e

    @classmethod
    def savePuertas(cls, almacen_id, puertas_agregadas):
        almacen = Almacen.query.get(almacen_id)
        if not almacen:
            return jsonify({'error': 'Almacén no encontrado'}), 404

        puertas_actuales = {
            puerta.nombre: puerta for puerta in almacen.puertas}

        for puerta in list(puertas_actuales):
            if puerta not in [p['nombre'] for p in puertas_agregadas]:
                puerta_eliminar = puertas_actuales[puerta]
                db.session.delete(puerta_eliminar)

        for puerta_data in puertas_agregadas:
            if puerta_data['nombre'] not in puertas_actuales:
                nueva_puerta = Puerta(
                    nombre=puerta_data['nombre'], estado_id=1, almacen_id=almacen_id)
                db.session.add(nueva_puerta)

        db.session.commit()
        return jsonify({'message': 'Puertas guardadas con éxito'}), 200
    

    @classmethod
    def updatePuertaEstado(cls, puerta_id):
        try:
            puerta = Puerta.query.get(puerta_id)
            if puerta:
                puerta.estado_id = 2 
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
