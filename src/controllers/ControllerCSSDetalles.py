from models import AlmacenCSSDetalles
from db import db

class ControllerCSSDetalles:
    
    @classmethod
    def createCSSDetalles(cls, almacen_id, detalles_css):
        try:
            nuevo_detalle_css = AlmacenCSSDetalles(
                top=detalles_css['top'],
                left_pos=detalles_css['leftPos'],
                width=detalles_css['width'],
                height=detalles_css['height'],
                color=detalles_css['color'],
                almacen_id=almacen_id
            )
            db.session.add(nuevo_detalle_css)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e