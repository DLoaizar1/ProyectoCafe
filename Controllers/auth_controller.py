from flask import Blueprint, request, render_template, redirect, session, url_for, flash
from Models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.find_by_username(username)
        if user and check_password_hash(user.Password, password):
            # Actualizar la fecha de inicio de sesión
            user.update_active_date()
            # Guardar el UserID en la sesión
            session['user_id'] = user.UserId
            flash('Login successful', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        user = User.create_user(username, password, email)
        flash('User registered successfully', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
