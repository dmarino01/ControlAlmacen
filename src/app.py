from flask import Flask, redirect, render_template, abort, flash, request, url_for
from config import Config, csrf
from db import db

import base64

from controllers.ControllerAlmacen import ControllerAlmacen

from blueprints.almacen_blueprint import almacen_bp
from blueprints.cliente_blueprint import cliente_bp
from blueprints.puertas_blueprint import puerta_bp
from blueprints.contrato_blueprint import contrato_bp

app = Flask(__name__)

app.config.from_object(Config)
app.url_map.strict_slashes = False

db.init_app(app)

app.register_blueprint(almacen_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(puerta_bp)
app.register_blueprint(contrato_bp)

@app.route('/')
@app.route('/index')
def index():
    almacenes = ControllerAlmacen.getAlmacenes()
    return render_template('index.html', almacenes=almacenes)

@app.route('/plantilla')
def plantilla():
    return render_template('layout_old.html')

@app.route('/error')
def trigger_error():
    abort(404)

@app.errorhandler(400)
def bad_request(error):
    return {"error 400": "Bad request"}, 400

@app.errorhandler(404)
def not_found(error):
    flash("Recurso no encontrado. Redirigiendo a la página de inicio.", 'error')
    return redirect(url_for('index')) 

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500

@app.template_filter('b64encode')
def b64encode_filter(data):
    if data is None:
        return None
    return base64.b64encode(data).decode('utf-8')

if __name__ == '__main__':
    csrf.init_app(app)
    app.run()