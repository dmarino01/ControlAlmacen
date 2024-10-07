from flask import Blueprint, json, request, jsonify

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

    try:
        for puerta in puertas_agregadas:
            # Crear o actualizar puertas en la base de datos
            # Ejemplo: verificar si la puerta ya existe y actualizar o crear
            nueva_puerta = Puerta(nombre=puerta['nombre'], estado_id=1, almacen_id=almacen_id)
            db.session.add(nueva_puerta)

        db.session.commit()
        return jsonify({'message': 'Puertas guardadas exitosamente.'})

    except Exception as e:
        db.session.rollback()  # Deshacer cambios en caso de error
        return jsonify({'error': str(e)}), 500