from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerCliente import ControllerCliente

from db import db

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes')
def clientes():
    data = ControllerCliente.getClientes()
    return render_template('components/clientes/index.html', clientes = data)

