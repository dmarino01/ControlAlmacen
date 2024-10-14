from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from controllers.ControllerContrato import ControllerContrato
from controllers.ControllerCliente import ControllerCliente
from controllers.ControllerAlmacen import ControllerAlmacen
from controllers.ControllerPuerta import ControllerPuerta


contrato_bp = Blueprint('contrato', __name__)

@contrato_bp.route('/contratos')
def contratos():
    data = ControllerContrato.getContratos()
    clientes = ControllerCliente.getClientes()
    almacenes = ControllerAlmacen.getAlmacenes()
    return render_template('components/contratos/index.html', contratos=data, clientes=clientes, almacenes=almacenes)


@contrato_bp.route('/almacen/<int:id>/puertas')
def get_puertas_by_almacen(id):
    try:
        puertas = ControllerPuerta.getPuertasPorAlmacen(id, 1)
        puertas_data = [{'id': puerta.id, 'nombre': puerta.nombre} for puerta in puertas]
        return jsonify(puertas_data)
    except Exception as e:
        print(f"Error fetching puertas: {e}")
        return jsonify([]), 500
    

@contrato_bp.route('/eliminar_contrato/<int:id>', methods=['GET', 'POST'])
def eliminar_contrato(id):
    if request.method == 'POST':
        try:
            ControllerContrato.deleteContrato(id)        
        except Exception as e:
            flash(f'Error al eliminar el contrato: {str(e)}', 'error')
        return redirect(url_for('contrato.contratos'))