from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerCliente import ControllerCliente
from sqlalchemy import exc

from db import db

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
        try:
            ControllerCliente.createCliente(nombre, contacto)
            return redirect(url_for('cliente.clientes'))
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('cliente.clientes'))
        except exc.IntegrityError:
            flash('Error de integridad: el cliente ya existe.', 'error')
            return redirect(url_for('cliente.clientes'))
        

@cliente_bp.route('/editar_cliente/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form['contacto']
        try:
            ControllerCliente.updateCliente(nombre, contacto, id)
            return redirect(url_for('cliente.clientes'))
        except Exception as e:
            flash(f'Error al actualizar el cliente: {str(e)}', 'error')
            return redirect(url_for('cliente.clientes'))
        
@cliente_bp.route('/eliminar_cliente/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):
    if request.method == 'POST':
        try:
            ControllerCliente.deleteCliente(id)
            return redirect(url_for('cliente.clientes'))
        except Exception as e:
            flash(f'Error al eliminar el cliente: {str(e)}', 'error')
            return redirect(url_for('cliente.clientes'))
