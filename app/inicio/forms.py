from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, SelectField, BooleanField 
from wtforms.validators import Optional, Length, Required, DataRequired, URL


class InicioForm(FlaskForm):
    name = StringField('Name', validators=[Optional(), Length(1, 64)])
    location = StringField('Location', validators=[Optional(), Length(1, 64)])
    bio = TextAreaField('Bio')
    submit = SubmitField('Submit')
    selecionaGrafico = SelectField('Status do Pedido', choices=[])
    selecionaSemanas = SelectField('Semanas', choices=[('Aberto','Aberto'),('Em produção','Em produção'),('Partiu para entrega','Partiu para entrega'),('Finalizado','Finalizado'),('Pago','Pago')])
    responsavel = SelectField('Vendedor', choices=[('Aberto','Aberto'),('Em produção','Em produção'),('Partiu para entrega','Partiu para entrega'),('Finalizado','Finalizado'),('Pago','Pago')])
class viewForm(FlaskForm):

    cliente = BooleanField('Cliente')
    fornecedor = BooleanField('Fornecedor')
    funcionario = BooleanField('Funcionario')
    pedido = BooleanField('Pedidos')    
    orcamento = BooleanField('Orçamentos')
    estoque = BooleanField('Estoque')
    pagamentos = BooleanField('Contas a pagar')
    recebimentos = BooleanField('Contas a receber')
    graficoPedidos = BooleanField('Grafico de pedidos')

    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')

