"""Adicionado campo nome ao modelo Usuario

Revision ID: 4c9422dd9871
Revises: 
Create Date: 2024-11-21 01:24:51.611161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c9422dd9871'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_despesa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descricao')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('senha', sa.String(length=128), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('palavra_chave', sa.String(length=50), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('resetar_senha', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('despesa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('tipo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tipo_id'], ['tipo_despesa.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receita',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receita')
    op.drop_table('despesa')
    op.drop_table('usuario')
    op.drop_table('tipo_despesa')
    # ### end Alembic commands ###
