from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Receita, Despesa, TipoDespesa
from app import db
from datetime import datetime

despesas = Blueprint('despesas', __name__)

@despesas.route('/')
def home():
    # Verifica se o usuário está logado
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    # Recupera despesas e receitas do usuário logado (garantindo listas vazias se não houver dados)
    despesas = Despesa.query.filter_by(usuario_id=current_user.id).all() or []
    receitas = Receita.query.filter_by(usuario_id=current_user.id).all() or []

    # Calcula o total de despesas e receitas
    total_despesas = sum([d.valor for d in despesas]) if despesas else 0
    total_receitas = sum([r.valor for r in receitas]) if receitas else 0

    # Agrupamento de despesas por tipo
    tipos_despesas = db.session.query(
        TipoDespesa.descricao,
        db.func.sum(Despesa.valor)
    ).join(Despesa).filter(Despesa.usuario_id == current_user.id).group_by(TipoDespesa.descricao).all()

    tipos_labels = [t[0] for t in tipos_despesas] if tipos_despesas else []
    tipos_values = [t[1] for t in tipos_despesas] if tipos_despesas else []

    despesas_labels = [d.descricao for d in despesas] if despesas else []
    despesas_values = [d.valor for d in despesas] if despesas else []

    # Renderiza a página inicial com os dados
    return render_template(
        'home.html',
        despesas=despesas,
        receitas=receitas,
        total_despesas=total_despesas,
        total_receitas=total_receitas,
        tipos_labels=tipos_labels,
        tipos_values=tipos_values,
        despesas_labels=despesas_labels,
        despesas_values=despesas_values
    )

@despesas.route('/despesas/nova', methods=['GET', 'POST'])
@login_required
def nova_despesa():
    tipos = TipoDespesa.query.all()
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        data = request.form.get('data')
        tipo_id = request.form.get('tipo_id')

        # Converte a data de string para datetime.date
        data = datetime.strptime(data, '%Y-%m-%d').date()

        nova_despesa = Despesa(
            usuario_id=current_user.id,
            descricao=descricao,
            valor=float(valor),  # Garante que o valor seja float
            data=data,
            tipo_id=int(tipo_id)  # Garante que o tipo_id seja inteiro
        )
        db.session.add(nova_despesa)
        db.session.commit()
        flash('Despesa cadastrada com sucesso!', 'success')
        return redirect(url_for('despesas.home'))
    return render_template('despesas/nova_despesa.html', tipos=tipos)

@despesas.route('/despesas/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_despesa(id):
    despesa = Despesa.query.get(id)
    if despesa and despesa.usuario_id == current_user.id:
        db.session.delete(despesa)
        db.session.commit()
        flash('Despesa excluída com sucesso!', 'success')
    else:
        flash('Ação não autorizada.', 'danger')
    return redirect(url_for('despesas.home'))
