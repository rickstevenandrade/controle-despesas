from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Usuario
from app import db, bcrypt, login_manager

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.check_senha(senha):
            if usuario.resetar_senha:
                flash('Sua senha deve ser redefinida antes de continuar.', 'warning')
                return redirect(url_for('auth.redefinir_senha'))
            login_user(usuario)
            return redirect(url_for('despesas.home'))
        flash('Credenciais inválidas', 'danger')
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmar_senha = request.form.get('confirmar_senha')
        palavra_chave = request.form.get('palavra_chave')  # Captura a palavra-chave

        # Validação básica
        if not nome or not email or not senha or not confirmar_senha or not palavra_chave:
            flash('Todos os campos são obrigatórios!', 'danger')
            return render_template('auth/cadastro.html')

        if senha != confirmar_senha:
            flash('As senhas não coincidem!', 'danger')
            return render_template('auth/cadastro.html')

        # Verifica se o e-mail já está cadastrado
        if Usuario.query.filter_by(email=email).first():
            flash('E-mail já está em uso.', 'danger')
            return render_template('auth/cadastro.html')

        # Criação do novo usuário
        novo_usuario = Usuario(nome=nome, email=email, palavra_chave=palavra_chave)
        novo_usuario.set_senha(senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/cadastro.html')

@auth.route('/recuperar-senha', methods=['GET', 'POST'])
def recuperar_senha():
    if request.method == 'POST':
        email = request.form.get('email')
        palavra_chave = request.form.get('palavra_chave')
        nova_senha = request.form.get('nova_senha')
        confirmar_senha = request.form.get('confirmar_senha')

        # Validação básica
        if not email or not palavra_chave or not nova_senha or not confirmar_senha:
            flash('Todos os campos são obrigatórios!', 'danger')
            return render_template('auth/recuperar_senha.html')

        if nova_senha != confirmar_senha:
            flash('As senhas não coincidem!', 'danger')
            return render_template('auth/recuperar_senha.html')

        # Verifica se o usuário existe e a palavra-chave está correta
        usuario = Usuario.query.filter_by(email=email, palavra_chave=palavra_chave).first()
        if not usuario:
            flash('E-mail ou palavra-chave inválidos.', 'danger')
            return render_template('auth/recuperar_senha.html')

        # Atualiza a senha do usuário
        usuario.set_senha(nova_senha)
        db.session.commit()

        flash('Senha atualizada com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/recuperar_senha.html')
