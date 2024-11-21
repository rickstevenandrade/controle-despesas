from app import db, bcrypt
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    palavra_chave = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    resetar_senha = db.Column(db.Boolean, default=False)

    def set_senha(self, senha):
        self.senha = bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_senha(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)

class Despesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.Date, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_despesa.id'), nullable=False)
    
    # Relacionamento com TipoDespesa
    tipo = db.relationship('TipoDespesa', backref='despesas', lazy=True)

class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.Date, nullable=False)

class TipoDespesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), unique=True, nullable=False)
