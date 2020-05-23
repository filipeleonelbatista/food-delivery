from flask_wtf import Form, FlaskForm

from wtforms import Form as NoCsrfForm
from wtforms import StringField, TextAreaField, SubmitField, FormField, FieldList, SelectField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class confirmForm(FlaskForm):
    s = SubmitField("Sim")
    n = SubmitField("Não")

class itensForm(NoCsrfForm):
    quantidade = StringField('Quantidade', validators=[Optional(), Length(1, 64)])
    produto = StringField('Produto', validators=[Optional(), Length(1, 64)])
    precoUnitario = StringField('Preço Unitário', validators=[Optional(), Length(1, 64)])
    precoTotal = StringField('Preço Total', validators=[Optional(), Length(1, 64)])

class pedidoForm(FlaskForm):
    cliente = StringField('Cliente', validators=[Optional(), Length(1, 64)])

    itens = FieldList(FormField(itensForm),  min_entries = 10)

    subTotal = StringField('Subtotal', validators=[Optional(), Length(1, 64)])
    frete = StringField('Frete', validators=[Optional(), Length(1, 64)])
    descontoPercentual = StringField('Desconto', validators=[Optional(), Length(1, 64)])
    total = StringField('Total', validators=[Optional(), Length(1, 64)])

    formasPagamento = SelectField('Formas de pagamento', choices=[('A vista','A vista'),('Boleto','Boleto'),('Link de pagamento','Link de pagamento'), ('Cartão de Crédito','Cartão de Crédito'),('Cartão de Débito','Cartão de Débito')])
    statusPedido = SelectField('Status do Pedido', choices=[('Aberto','Aberto'),('Em produção','Em produção'),('Partiu para entrega','Partiu para entrega'),('Finalizado','Finalizado'),('Pago','Pago')])

    observacao = TextAreaField('Observação')
    
    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")

