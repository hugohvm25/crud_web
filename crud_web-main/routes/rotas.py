from flask import Blueprint, render_template

rotas_bp = Blueprint('rotas', __name__)

@rotas_bp.route('/')
def home():
    return render_template('index.html')
