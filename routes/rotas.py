from flask import Blueprint, render_template

#é uma maneira de organizar e modularizar o código no Flask. Ele permite agrupar as rotas, tornando o código mais fácil de manter.
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')
