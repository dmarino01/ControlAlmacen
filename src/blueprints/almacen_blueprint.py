from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
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
    return render_template('components/almacenes/index.html', almacenes=data, estadoPuertas=estadoPuertas)


@almacen_bp.route('/almacenes/<int:id>/puertas', methods=['GET'])
def obtener_puertas(id):
    puertas = ControllerPuerta.getPuertasPorAlmacen(id)
    puertas_data = [puerta.to_dict() for puerta in puertas]
    return jsonify(puertas_data)


@almacen_bp.route('/crear_almacen', methods=['GET', 'POST'])
def agregar_almacen():
    if request.method == 'POST':
        # Recibir los datos del formulario
        nombre_almacen = request.form['almacenNombre']
        css_detalles = {}

        if request.form.get('top'):
            css_detalles['top'] = request.form['top']
        if request.form.get('leftPos'):
            css_detalles['leftPos'] = request.form['leftPos']
        if request.form.get('width'):
            css_detalles['width'] = request.form['width']
        if request.form.get('height'):
            css_detalles['height'] = request.form['height']
        if request.form.get('color'):
            css_detalles['color'] = request.form['color']
        # Guardar los datos usando los controladores
        try:
            almacen_id = ControllerAlmacen.createAlmacen(nombre_almacen)
            if css_detalles:
                ControllerCSSDetalles.createCSSDetalles(almacen_id, css_detalles)
        except Exception as e:
            flash(f'Error al crear el almacen: {str(e)}', 'error')
        return redirect(url_for('almacen.almacenes'))


@almacen_bp.route('/editar_almacen/<int:id>', methods=['GET', 'POST'])
def editar_almacen(id):
    if request.method == 'POST':
        nombre_almacen = request.form['almacenNombre']

        css_detalles = {}

        if request.form.get('top'):
            css_detalles['top'] = request.form['top']
        if request.form.get('leftPos'):
            css_detalles['leftPos'] = request.form['leftPos']
        if request.form.get('width'):
            css_detalles['width'] = request.form['width']
        if request.form.get('height'):
            css_detalles['height'] = request.form['height']
        if request.form.get('color'):
            css_detalles['color'] = request.form['color']
        try:
            almacen_id = ControllerAlmacen.updateAlmacen(id, nombre_almacen)
            ControllerCSSDetalles.updateCSSDetalles(id, css_detalles)
        except Exception as e:
            flash(f'Error al actualizar el almacen: {str(e)}', 'error')
        return redirect(url_for('almacen.almacenes'))


@almacen_bp.route('/eliminar_almacen/<int:id>', methods=['GET', 'POST'])
def eliminar_almacen(id):
    if request.method == 'POST':
        try:
            ControllerAlmacen.deleteAlmacen(id)
        except Exception as e:
            flash(f'Error al eliminar el almacen: {str(e)}', 'error')
        return redirect(url_for('almacen.almacenes'))
