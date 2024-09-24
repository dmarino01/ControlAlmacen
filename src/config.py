from flask_wtf.csrf import CSRFProtect

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:123@localhost/BDControlAlmacen?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=True

csrf = CSRFProtect()