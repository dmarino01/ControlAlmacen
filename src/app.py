from flask import Flask, render_template, abort
from config import Config, csrf
from db import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

from models.puerta import Puerta
from models.almacen import Almacen
from models.almacen_css_detalles import AlmacenCSSDetalles
from models.puerta_estado import PuertaEstado
from models.cliente import Cliente

@app.route('/')
def index():
    almacenes = Almacen.query.all()
    return render_template('index.html', almacenes=almacenes)

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500

@app.errorhandler(400)
def bad_request(error):
    return {"error": "Bad request"}, 400

@app.route('/error')
def trigger_error():
    abort(404)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)