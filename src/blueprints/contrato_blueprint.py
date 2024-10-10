from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.ControllerContrato import ControllerContrato
from sqlalchemy import exc

from db import db

contrato_bp = Blueprint('contrato', __name__)

@contrato_bp.route('/contratos')
def contratos():
    data = ControllerContrato.getContratos()
    return render_template('components/contratos/index.html', contratos=data)