from flask import Flask, render_template, abort
from config import Config, csrf
from db import db

from controllers.ControllerAlmacen import ControllerAlmacen

from blueprints.almacen_blueprint import almacen_bp
from blueprints.cliente_blueprint import cliente_bp

app = Flask(__name__)

app.config.from_object(Config)
app.url_map.strict_slashes = False

db.init_app(app)

app.register_blueprint(almacen_bp)
app.register_blueprint(cliente_bp)

@app.route('/')
@app.route('/index')
def index():
    almacenes = ControllerAlmacen.getAlmacenes()
    return render_template('index.html', almacenes=almacenes)

@app.route('/error')
def trigger_error():
    abort(404)

@app.errorhandler(400)
def bad_request(error):
    return {"error": "Bad request"}, 400

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"error": "Internal server error"}, 500

if __name__ == '__main__':
    csrf.init_app(app)
    app.run()