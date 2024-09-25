import os
import pyodbc

# Conexión a MySQL
class config:
    # Configuración de SQLAlchemy para conexión a SQL Server
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://Admin:1234@DESKTOP-EDAF4HI/Tesis?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones para mejorar el rendimiento
    SECRET_KEY = 'FSERNAL01'  # Clave secreta para las sesiones
    # Configuración de Flask-Mail para envío de correos electrónicos
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'cafePregunta@outlook.com'  # Reemplaza con tu email de Outlook
    MAIL_PASSWORD = 'ZE4V8-WT2LX-82EVE-GXDQR-3F3E8'  # Reemplaza con tu contraseña de Outlook
    MAIL_DEFAULT_SENDER = 'cafePregunta@outlook.com' 
    # Configuración de Flask-User para el manejo de usuarios



