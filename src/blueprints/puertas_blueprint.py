from flask import Blueprint, json, request, jsonify

from models import Puerta, Almacen

from controllers.ControllerPuerta import ControllerPuerta

from db import db

puerta_bp = Blueprint('puerta', __name__)


@puerta_bp.route('/almacenes/<int:id>/puertas', methods=['GET'])
def obtener_puertas(id):
    puertas = ControllerPuerta.getPuertasPorAlmacen(id)
    puertas_data = [puerta.to_dict() for puerta in puertas]
    return jsonify(puertas_data)


@puerta_bp.route('/guardarPuertas', methods=['POST'])
def guardar_puertas():


    return jsonify({'message': 'Puertas guardadas exitosamente'})
