from flask import Flask
# faz a conexão com as rotas
from routes.rotas import home_bp
from db.db import db, init_db
from models.usuario import Usuario


app = Flask(__name__)

# Inicializar o banco de dados
init_db(app)

# Registra o Blueprint no aplicativo principal, conectando as rotas definidas no home.py ao servidor Flask.
app.register_blueprint(home_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco de dados
# Inicia o servidor web local com o modo de depuração ativado, o que facilita o desenvolvimento, mostrando erros diretamente no navegador.
    app.run(debug=True)