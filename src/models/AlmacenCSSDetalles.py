from db import db

class AlmacenCSSDetalles(db.Model):
    __tablename__ = 'almacen_css_detalles'

    id = db.Column(db.Integer, primary_key=True)
    top = db.Column(db.Integer)
    left_pos = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    color = db.Column(db.String(20))
    almacen_id = db.Column(db.Integer, db.ForeignKey('almacenes.id'))

    almacen = db.relationship('Almacen', back_populates='almacenCSSDetalles', lazy=True)