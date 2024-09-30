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
def create_client():
    if request.method == 'GET':
        return redirect(url_for("cliente.clientes"))
    
    if request.method == 'POST':

        nombre = request.form['nombre']
        contacto = request.form['contacto']

        try:
            # Save the new client to the database
            # (Your database logic here)
            flash('¡Cliente creado exitosamente!', 'success')
            return redirect(url_for('cliente.clientes'))
        except exc.IntegrityError:
            flash('Error de integridad: el cliente ya existe.', 'error')
            return redirect(url_for('cliente.clientes'))
        except Exception:
            raise Exception


@cliente_bp.route('/editar_cliente/<int:id>', methods=['POST'])
def edit_client(id):
    nombre = request.form['nombre']
    contacto = request.form['contacto']
    # Update the client in the database
    # (Your database logic here)
    return redirect('/clientes')
