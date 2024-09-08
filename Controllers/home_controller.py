from flask import Blueprint, render_template, redirect, url_for, session

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    print("Checking user session...")
    if 'user_id' not in session:
        print("User not logged in, redirecting to login...")
        return redirect(url_for('auth.login'))
    print("User is logged in, displaying home page.")
    return render_template('home.html')
