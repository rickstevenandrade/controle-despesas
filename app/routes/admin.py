from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import Usuario
from app import db

admin = Blueprint('admin', __name__)

@admin.route('/admin/usuarios')
@login_required
def usuarios():
    if not current_user.is_admin:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('despesas.home'))

    usuarios = Usuario.query.all()
    return render_template('admin/usuarios.html', usuarios=usuarios)

@admin.route('/admin/usuarios/tornar-admin/<int:id>')
@login_required
def tornar_admin(id):
    if not current_user.is_admin:
        flash('Acesso negado.', 'danger')
        return redirect(url_for('despesas.home'))

    usuario = Usuario.query.get(id)
    if usuario:
        usuario.is_admin = True
        db.session.commit()
        flash('Usuário promovido a administrador.', 'success')
    return redirect(url_for('admin.usuarios'))
