from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario
from db.db import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.senha, password):
            session['user_id'] = user.id
            print(f"Usuário logado: {session.get('user_id')}")  # Debug
            return redirect(url_for('rotas.welcome'))
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

        # Verificar se o usuário já existe
        user_exists = Usuario.query.filter_by(email=email).first()
        if user_exists:
            flash('Email já cadastrado.', 'error')
            return render_template('register.html', error='Email já cadastrado.')

        # Criar uma nova instância de Usuario com senha criptografada
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = Usuario(nome=nome, email=email, senha=hashed_password)
        
        # Adicionar o usuário ao banco de dados
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # Reverter mudanças se houver um erro
            flash(f'Ocorreu um erro: {str(e)}', 'error')
            return render_template('register.html', error='Erro ao registrar usuário.')

        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


