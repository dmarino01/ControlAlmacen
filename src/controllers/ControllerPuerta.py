from models import Puerta, Almacen
from flask import jsonify
from db import db


class ControllerPuerta:

    @classmethod
    def createPuertas(cls, almacen_id, puertas_data, estado_puertas):
        try:
            for nombre_puerta, estado_puerta in zip(puertas_data, estado_puertas):
                nueva_puerta = Puerta(
                    nombre=nombre_puerta, estado_id=estado_puerta, almacen_id=almacen_id)
                db.session.add(nueva_puerta)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e

    @classmethod
    def getPuertasPorAlmacen(cls, id):
        try:
            puertas = Puerta.query.filter_by(almacen_id=id).all()
            return puertas
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e


    @classmethod
    def savePuertas(cls, almacen_id, puertas_agregadas):
        # Obtener el almacén
        almacen = Almacen.query.get(almacen_id)
        if not almacen:
            return jsonify({'error': 'Almacén no encontrado'}), 404

        # Actualizar puertas del almacén
        puertas_actuales = {puerta.nombre: puerta for puerta in almacen.puertas}

        # Remover puertas que ya no están en la lista
        for puerta in list(puertas_actuales):
            if puerta not in [p['nombre'] for p in puertas_agregadas]:
                puerta_eliminar = puertas_actuales[puerta]
                db.session.delete(puerta_eliminar)

        # Agregar nuevas puertas
        for puerta_data in puertas_agregadas:
            if puerta_data['nombre'] not in puertas_actuales:
                nueva_puerta = Puerta(nombre=puerta_data['nombre'], estado_id=1, almacen_id=almacen_id)  # Ajustar estado_id si es necesario
                db.session.add(nueva_puerta)

        db.session.commit()
        return jsonify({'message': 'Puertas guardadas con éxito'}), 200