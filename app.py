from flask import Flask
from Models import db  # Asegúrate de importar db desde models/__init__.py
from config import config
from Controllers.home_controller import home_bp
from Controllers.auth_controller import auth_bp
from Controllers.chat_controler import chat_bp
from flask_mail import Mail
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.secret_key = 'FSERNAL01' 

    db.init_app(app)
    mail.init_app(app) 

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp)  
    app.register_blueprint(chat_bp, url_prefix='/chat')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
