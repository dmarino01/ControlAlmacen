from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerCliente import ControllerCliente
from sqlalchemy import exc

import base64

cliente_bp = Blueprint('cliente', __name__)


@cliente_bp.route('/clientes')
def clientes():
    data = ControllerCliente.getClientes()
    return render_template('components/clientes/index.html', clientes=data)


@cliente_bp.route('/crear_cliente', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        logo_file = request.files['logo']
        
        if logo_file:
            logo = logo_file.read()
        else:
            logo = None

        try:
            ControllerCliente.createCliente(nombre, contacto, logo)
        except ValueError as e:
            flash(str(e), 'error')
        except exc.IntegrityError:
            flash('Error de integridad: el cliente ya existe.', 'error')
        return redirect(url_for('cliente.clientes'))
        

@cliente_bp.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        logo_file = request.files['logo']
        
        if logo_file:
            logo = logo_file.read()
        else:
            logo = None

        try:
            ControllerCliente.updateCliente(id, nombre, contacto, logo)   
        except Exception as e:
            flash(f'Error al actualizar el cliente: {str(e)}', 'error')
        return redirect(url_for('cliente.clientes'))
        
        
@cliente_bp.route('/eliminar_cliente/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):
    if request.method == 'POST':
        try:
            ControllerCliente.deleteCliente(id)        
        except Exception as e:
            flash(f'Error al eliminar el cliente: {str(e)}', 'error')
        return redirect(url_for('cliente.clientes'))


@cliente_bp.route('/remover_logo/<int:id>', methods=['GET', 'POST'])
def remover_logo(id):
    if request.method == 'GET':
        try:
            ControllerCliente.removeLogo(id)
        except Exception as e:
            flash(f'Error al eliminar el logo: {str(e)}', 'error')
    return redirect(url_for('cliente.clientes'))