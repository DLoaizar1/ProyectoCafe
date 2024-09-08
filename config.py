import os
import pyodbc

# Conexión a MySQL
class config:
    # Configuración de SQLAlchemy para conexión a SQL Server
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://Admin:1234@DESKTOP-EDAF4HI/Tesis?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones para mejorar el rendimiento
    SECRET_KEY = 'FSERNAL01'  # Clave secreta para las sesiones
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'loaizad65@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'Loaiza01*')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'



