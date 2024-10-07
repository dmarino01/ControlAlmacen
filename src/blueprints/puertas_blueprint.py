from flask import Blueprint, flash, json, request, jsonify

from controllers.ControllerPuerta import ControllerPuerta
from models import Puerta

from db import db

puerta_bp = Blueprint('puerta', __name__)


@puerta_bp.route('/almacenes/<int:id>/puertas', methods=['GET'])
def obtener_puertas(id):
    puertas = ControllerPuerta.getPuertasPorAlmacen(id)
    puertas_data = [puerta.to_dict() for puerta in puertas]
    return jsonify(puertas_data)


@puerta_bp.route('/guardarPuertas', methods=['POST'])
def guardar_puertas():
    data = request.json

    almacen_id = data.get('almacenId')
    puertas_agregadas = data.get('puertasAgregadas', [])
    puertas_eliminadas = data.get('puertasEliminadas', [])
    
    try:
        # Asegúrate de no modificar contratos aquí
        for puerta in puertas_agregadas:
            nueva_puerta = Puerta(nombre=puerta['nombre'], estado_id=1, almacen_id=almacen_id)  # Ajusta según tus requisitos
            db.session.add(nueva_puerta)

        for puerta_id in puertas_eliminadas:
            puerta_a_eliminar = Puerta.query.get(puerta_id)
            if puerta_a_eliminar:
                db.session.delete(puerta_a_eliminar)

        db.session.commit()
        flash("Puertas guardadas exitosamente.", "success")
        return jsonify({"message": "Puertas guardadas exitosamente."})

    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return jsonify({"error": "Error al guardar puertas."}), 500
    
    