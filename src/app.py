from flask import Flask, render_template, abort
from config import Config, csrf
from db import db

from controllers.ControllerAlmacen import ControllerAlmacen

from blueprints.almacen_blueprint import almacen_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(almacen_bp)

@app.route('/')
def index():
    almacenes = ControllerAlmacen.getAlmacenes()
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
    app.run()