from flask import Blueprint, render_template, session, redirect, url_for
from models.usuario import Usuario

rotas_bp = Blueprint('rotas', __name__)

@rotas_bp.route('/welcome')
def welcome():
    user_id = session.get('user_id')
    if user_id:
        user = Usuario.query.get(user_id)
        return render_template('welcome.html', user=user)
    return redirect(url_for('auth.login'))

