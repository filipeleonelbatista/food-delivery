from flask_wtf import Form, FlaskForm
from wtforms import StringField, StringField, TextAreaField, SubmitField, DateField, IntegerField, SelectField, RadioField, BooleanField, FileField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class excluirForm(FlaskForm):
    s = SubmitField("Sim")
    n = SubmitField("Não")

class categoriaForm(FlaskForm):
    categoria = StringField('Categoria', validators=[Optional(), Length(1, 64)]) 

    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')

class editarViewForm(FlaskForm):
    nomeProduto = BooleanField('Nome do produto')
    descricaoProduto = BooleanField('Descriçao')
    precoVenda = BooleanField('Preço de venda')

    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')

class EstoqueForm(FlaskForm):
    nomeProduto = StringField('Nome do produto', validators=[Optional(), Length(1, 64)]) 
    descricaoProduto = StringField('Descrição do produto', validators=[Optional(), Length(1, 64)])
    precoVenda = StringField('Preço de Venda ao consumidor', validators=[Optional(), Length(1,64)])
    categoria = SelectField(u'Categoria', choices=[])

    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')
 
    imagem        = FileField(u'Foto do produto')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class FotoUploadForm(FlaskForm):
    image        = FileField(u'Image File')
    enviar = SubmitField('Enviar Foto')
    descartar = SubmitField('Descartar Foto')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)