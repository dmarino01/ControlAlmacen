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

    @classmethod
    def updateCSSDetalles(cls, almacen_id, detalles_css):
        try:
            # Verificar si ya existen detalles CSS para este almacén
            css_detalle = AlmacenCSSDetalles.query.filter_by(
                almacen_id=almacen_id).first()

            # Verificar si todos los campos CSS están vacíos
            if all(not detalles_css.get(key) for key in ['top', 'leftPos', 'width', 'height', 'color']):
                if css_detalle:
                    # Si existen detalles y todos los campos están vacíos, eliminar el detalle
                    db.session.delete(css_detalle)
                db.session.commit()
                return

            if css_detalle:
                # Si existen detalles previos, se actualizan
                if 'top' in detalles_css:
                    css_detalle.top = detalles_css['top']
                if 'leftPos' in detalles_css:
                    css_detalle.left_pos = detalles_css['leftPos']
                if 'width' in detalles_css:
                    css_detalle.width = detalles_css['width']
                if 'height' in detalles_css:
                    css_detalle.height = detalles_css['height']
                if 'color' in detalles_css:
                    css_detalle.color = detalles_css['color']
            else:
                # Si no existen, se crean nuevos detalles
                nuevo_css_detalle = AlmacenCSSDetalles(
                    top=detalles_css.get('top'),
                    left_pos=detalles_css.get('leftPos'),
                    width=detalles_css.get('width'),
                    height=detalles_css.get('height'),
                    color=detalles_css.get('color'),
                    almacen_id=almacen_id
                )
                db.session.add(nuevo_css_detalle)

            # Guardar cambios en la base de datos
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"General error: {e}")
            raise e
