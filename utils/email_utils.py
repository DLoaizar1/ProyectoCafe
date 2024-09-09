from flask import current_app, url_for
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from Models.user_model import User

mail = Mail()

def send_reset_email(user):
    try:
        token = generate_reset_token(user.Email)
        msg = Message('Reset Your Password', sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[user.Email])
        link = url_for('auth.reset_password', token=token, _external=True)
        msg.body = f'Your link to reset the password is {link}. If you did not request a password reset, please ignore this email.'
        
        mail.send(msg)
        print(f"Correo enviado a {user.Email} con el enlace: {link}")  # Punto de depuración
    except Exception as e:
        print(f"Error al enviar el correo: {e}")  # Punto de depuración en caso de error

def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    print(f"Generando token para {email}")  # Punto de depuración
    return serializer.dumps(email, salt='password-reset-salt')

def verify_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        print(f"Token verificado para {email}")  # Punto de depuración
    except Exception as e:
        print(f"Error al verificar el token: {e}")  # Punto de depuración en caso de error
        return None
    return User.find_by_email(email)
