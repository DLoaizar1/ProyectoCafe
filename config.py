import os
#import pyodbc

# Conexión a MySQL
class config:
    # Configuración de SQLAlchemy para conexión a SQL Server
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://Admin:1234@DESKTOP-F4S97L6/Tesis?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'  
    MAIL_PASSWORD = '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'   
    MAIL_DEFAULT_SENDER = 'fernandos0010@hotmail.com'

#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


