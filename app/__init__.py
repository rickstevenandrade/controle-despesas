import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate



# Instâncias globais
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))    # Configura o Flask para ler a variável de ambiente PORT (para produção)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    # Importar e registrar Blueprints
    from app.routes.auth import auth
    from app.routes.admin import admin
    from app.routes.despesas import despesas
    from app.routes.receitas import receitas

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(despesas)
    app.register_blueprint(receitas)

    return app
