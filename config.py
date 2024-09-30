import os
#import pyodbc

# Conexión a MySQL
class config:
    # Configuración de SQLAlchemy para conexión a SQL Server
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://Admin:1234@DESKTOP-EDAF4HI/Tesis?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'  
    MAIL_PASSWORD = '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'  
    MAIL_DEFAULT_SENDER = 'fernandos0010@hotmail.com'




