from app import create_app, db
from app.models import Usuario, TipoDespesa

app = create_app()

with app.app_context():
    db.create_all()

    # Criar usuário administrador padrão
    if not Usuario.query.filter_by(email='admin@example.com').first():
        admin = Usuario(nome='Administrador', email='admin@example.com', palavra_chave='admin', is_admin=True)
        admin.set_senha('admin')
        db.session.add(admin)

    # Adicionar tipos de despesas padrão
    tipos_padrao = [
        'Alimentação', 'Supermercado', 'Restaurantes', 'Lanches', 'Bebidas',
        'Transporte', 'Combustível', 'Manutenção do Veículo', 'Transporte Público', 'Pedágios', 'Táxi/Aplicativos de Transporte',
        'Lazer', 'Cinema', 'Viagens', 'Shows e Eventos', 'Esportes', 'Assinaturas',
        'Educação', 'Cursos', 'Livros', 'Materiais Escolares', 'Mensalidades Escolares/Faculdades',
        'Saúde', 'Consultas Médicas', 'Medicamentos', 'Exames', 'Seguro Saúde',
        'Patrimônio', 'Seguro Residencial', 'Manutenção da Casa', 'Compra de Móveis', 'Eletrônicos',
        'Imóvel', 'Condomínio', 'IPTU', 'Reformas',
        'Aluguel', 'Aluguel Residencial', 'Aluguel de Equipamentos', 'Aluguel de Espaços',
        'Contas Fixas', 'Energia Elétrica', 'Água', 'Internet', 'Telefonia', 'TV a Cabo',
        'Investimentos e Finanças', 'Ações/Investimentos', 'Poupança', 'Juros', 'Pagamentos de Dívidas',
        'Cuidados Pessoais', 'Salão de Beleza', 'Cuidados com a Pele', 'Academia', 'Roupas', 'Sapatos',
        'Pets', 'Alimentação para Pets', 'Veterinário', 'Acessórios para Pets',
        'Família e Presentes', 'Presentes', 'Aniversários', 'Festas e Celebrações',
        'Tecnologia e Assinaturas', 'Softwares', 'Licenças', 'Hospedagem de Sites',
        'Doações e Filantropia', 'Doações para ONGs', 'Ofertas Religiosas', 'Ajuda a Familiares/Amigos'
    ]
    for descricao in tipos_padrao:
        if not TipoDespesa.query.filter_by(descricao=descricao).first():
            tipo = TipoDespesa(descricao=descricao)
            db.session.add(tipo)

    db.session.commit()
    print('Dados iniciais inseridos com sucesso!')
