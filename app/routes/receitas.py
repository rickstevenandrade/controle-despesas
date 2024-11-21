from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Receita
from app import db
from datetime import datetime

receitas = Blueprint('receitas', __name__)

@receitas.route('/receitas')
@login_required
def listar_receitas():
    receitas = Receita.query.filter_by(usuario_id=current_user.id).all()
    return render_template('receitas/listar_receitas.html', receitas=receitas)

@receitas.route('/receitas/nova', methods=['GET', 'POST'])
@login_required
def nova_receita():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        data = request.form.get('data')

        nova_receita = Receita(
            usuario_id=current_user.id,
            descricao=descricao,
            valor=float(valor),
            data=datetime.strptime(data, '%Y-%m-%d').date()
        )
        db.session.add(nova_receita)
        db.session.commit()
        flash('Receita cadastrada com sucesso!', 'success')
        return redirect(url_for('despesas.home'))
    return render_template('receitas/nova_receita.html')

@receitas.route('/receitas/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_receita(id):
    receita = Receita.query.get(id)
    if receita and receita.usuario_id == current_user.id:
        db.session.delete(receita)
        db.session.commit()
        flash('Receita excluída com sucesso!', 'success')
    else:
        flash('Ação não autorizada.', 'danger')
    return redirect(url_for('despesas.home'))
