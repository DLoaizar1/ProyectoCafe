from flask import Blueprint, request, render_template, redirect, session, url_for, flash
from Models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from utils.email_utils import send_reset_email, verify_reset_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.find_by_username(username)
        if user and check_password_hash(user.Password, password):
            user.update_active_date()
            session['user_id'] = user.UserId
            return redirect(url_for('home.home'))
        else:
            flash('Crrdenciales incorrectas', 'danger')  
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        user = User.create_user(username, password, email)
        session['user_id'] = user.UserId
        flash('Usuario registrado', 'success')
        return redirect(url_for('home.home'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))

#Funcionando inicio de sesión y registro de usuario

@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.find_by_email(email)
        if user:
            send_reset_email(user)  
            flash('Email enviado con instrucciones a su correo', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Correo no encontrado', 'danger')  
    return render_template('forgot_password.html')

# Restablecer Contraseña con token
@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = verify_reset_token(token)
    if not user:
        flash('El token ha expirado.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    if request.method == 'POST':
        password = generate_password_hash(request.form['password'])
        user.update_password(password)
        flash('Contraseña cambiada', 'success')
        return redirect(url_for('auth.login'))

    return render_template('reset_password.html')
