from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerAlmacen import ControllerAlmacen
from controllers.ControllerPuerta import ControllerPuerta
from controllers.ControllerCSSDetalles import ControllerCSSDetalles
from controllers.ControllerPuertaEstados import ControllerPuertaEstados

from db import db

almacen_bp = Blueprint('almacen', __name__)


@almacen_bp.route('/almacenes')
def almacenes():
    data = ControllerAlmacen.getAlmacenes()
    estadoPuertas = ControllerPuertaEstados.getPuertaEstados()
    return render_template('components/almacenes/index.html', almacenes=data, estadoPuertas = estadoPuertas)


@almacen_bp.route('/crear_almacen', methods=['GET', 'POST'])
def agregar_almacen():
    if request.method == 'POST':
        # Recibir los datos del formulario
        nombre_almacen = request.form.get('nombreAlmacen')
        puertas_data = request.form.getlist('nombrePuerta')
        estado_puertas = request.form.getlist('estadoPuerta')
        css_detalles = {
            'top': request.form.get('top'),
            'leftPos': request.form.get('leftPos'),
            'width': request.form.get('width'),
            'height': request.form.get('height'),
            'color': request.form.get('color')
        }
        # Guardar los datos usando los controladores
        almacen_id = ControllerAlmacen.createAlmacen(nombre_almacen)
        ControllerPuerta.createPuertas(almacen_id, puertas_data, estado_puertas)
        ControllerCSSDetalles.createCSSDetalles(almacen_id, css_detalles)
        flash('Almacén agregado exitosamente', 'success')
        return redirect(url_for('index'))
    return render_template('index')


@almacen_bp.route('/eliminar_almacen/<int:id>', methods=['GET', 'POST'])
def eliminar_almacen(id):
    if request.method == 'POST':
        try:
            ControllerAlmacen.deleteAlmacen(id)
            return redirect(url_for('almacen.almacenes'))
        except Exception as e:
            flash(f'Error al eliminar el almacen: {str(e)}', 'error')
            return redirect(url_for('almacen.almacenes'))