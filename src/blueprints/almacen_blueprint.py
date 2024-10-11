from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerAlmacen import ControllerAlmacen
from controllers.ControllerCSSDetalles import ControllerCSSDetalles
from controllers.ControllerPuertaEstados import ControllerPuertaEstados
from controllers.ControllerEmpresa import ControllerEmpresa


almacen_bp = Blueprint('almacen', __name__)


@almacen_bp.route('/almacenes')
def almacenes():
    data = ControllerAlmacen.getAlmacenes()
    estadoPuertas = ControllerPuertaEstados.getPuertaEstados()
    empresas = ControllerEmpresa.getEmpresas()
    return render_template('components/almacenes/index.html', almacenes=data, estadoPuertas=estadoPuertas, empresas=empresas)


@almacen_bp.route('/crear_almacen', methods=['GET', 'POST'])
def agregar_almacen():
    if request.method == 'POST':
        # Recibir los datos del formulario
        nombre = request.form['almacenNombre']
        empresa_id = request.form['almacenEmpresa']
        css_detalles = {
            'top': 0,
            'leftPos': 0,
            'width': 0,
            'height': 0,
            'color': '#000000'
        }

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
            almacen_id = ControllerAlmacen.createAlmacen(nombre, empresa_id)
            if css_detalles:
                ControllerCSSDetalles.createCSSDetalles(almacen_id, css_detalles)
        except Exception as e:
            #flash(f'Error al crear el almacen: {str(e)}', 'error')
            raise e
        return redirect(url_for('almacen.almacenes'))


@almacen_bp.route('/editar_almacen/<int:id>', methods=['GET', 'POST'])
def editar_almacen(id):
    if request.method == 'POST':
        nombre = request.form['almacenNombre']
        empresa_id = request.form['almacenEmpresa']

        css_detalles = {
            'top': 0,
            'leftPos': 0,
            'width': 0,
            'height': 0,
            'color': '#000000'
        }

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
            almacen_id = ControllerAlmacen.updateAlmacen(id, nombre, empresa_id)
            if css_detalles:
                ControllerCSSDetalles.updateCSSDetalles(id, css_detalles)
            else:
                ControllerCSSDetalles.updateCSSDetalles(id, {})
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
