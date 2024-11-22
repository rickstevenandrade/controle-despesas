# Controle de Finanças

O **Controle de Finanças** é uma aplicação web desenvolvida em **Python** com o framework **Flask**, projetada para facilitar o gerenciamento financeiro pessoal. A aplicação permite registrar receitas e despesas, categorizando-as e exibindo relatórios gráficos para uma visualização clara e objetiva.
Este projeto foi desenvolvido como parte das atividades da disciplina **Desenvolvimento Rápido de Aplicações em Python (ARA0095)**, ministrada pelo professor **Heleno Filho**.  

**Data de entrega:** 22/11/2024.
**Equipe:** Rick Andrade, 

---

## Recursos Oferecidos

### 1. Cadastro e Autenticação de Usuários
- Registro de novos usuários.
- Login seguro utilizando e-mail e senha.
- Recuperação de senha com palavra-chave personalizada.

### 2. Gerenciamento de Receitas e Despesas
- Registro de receitas e despesas com:
  - Descrição
  - Valor
  - Data
  - Tipo (para despesas)
- Possibilidade de excluir receitas e despesas diretamente na interface.

### 3. Gráficos
- **Gráfico de barras horizontal:** Exibe as despesas por valor.
- **Gráfico de barras horizontal:** Exibe as despesas categorizadas por tipo.
- **Gráfico de rosca:** Compara o total de despesas e receitas.

### 4. Interface Intuitiva
- Interface em **tema dark**.
- Botões de ação para cadastrar receitas e despesas.
- Visualização de tabelas responsivas para listar receitas e despesas.

---

## Estrutura do Projeto
###	Backend
-	Framework: **Flask**
-	Banco de Dados: **SQLite**
-	Gerenciamento de Migrações: **Flask-Migrate**
-	Criptografia de Senhas: **Flask-Bcrypt**
-	Controle de Sessões: **Flask-Login**

###	Frontend
-	Framework CSS: **Bootstrap**
-	Visualização de Dados: **Chart.js**

###	Scripts Auxiliares
-	seed.py: Popula o banco de dados com dados iniciais, como tipos de despesas.

---

## Como Utilizar
1.	Clone o projeto do repositório no GitHub.
2.	Configure o ambiente virtual e instale as dependências.
3.	Execute as migrações para configurar o banco de dados.
4.	Inicie o servidor Flask e acesse a aplicação no navegador.
5.	Crie uma conta, registre receitas e despesas, e visualize os relatórios.

###  Pré-requisitos
1.	**Python 3.8 ou superior** instalado.
2.	Ferramenta de gerenciamento de pacotes pip.
3.	Sistema operacional com suporte a sqlite3 (Windows, Linux ou macOS).

O passo a passo para clonar e configurar a aplicação está disponível no arquivo de apresentação **App_Web_Controle_de_Financas.pptx**.
