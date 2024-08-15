from flask import Flask
from db.db import init_db, db
from models.usuario import Usuario
from routes.rotas import rotas_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Necessário para sessões

# Inicializar o banco de dados
init_db(app)

# Registrar os Blueprints das rotas
app.register_blueprint(rotas_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
