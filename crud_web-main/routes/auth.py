from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario import Usuario
from db.db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Usuario.query.filter_by(email=email).first()

        if user and user.senha == password:
            return redirect(url_for('rotas.home'))
        else:
            flash('Email ou senha incorretos.', 'error')
            return render_template('login.html', error='Email ou senha incorretos.')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        password = request.form['password']

        # Verifica se o usuário já existe
        user_exists = Usuario.query.filter_by(email=email).first()
        if user_exists:
            flash('Email já cadastrado.', 'error')
            return render_template('register.html', error='Email já cadastrado.')

        # Cria um novo usuário
        new_user = Usuario(nome=nome, email=email, senha=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
