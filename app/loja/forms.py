from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField, BooleanField, IntegerField, DateField, DateTimeField, PasswordField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class AnuncioForm(FlaskForm):

    categoria = SelectField('Categoria', choices=[])
    destaque = BooleanField('Colocar anuncio em destaque?')
    titulo = StringField('Titulo do Anuncio', validators=[Optional(), Length(1, 64)])
    descricao = StringField('Descrição', validators=[Optional(), Length(1, 255)])
    precoVenda = StringField('Preço de Venda', validators=[Optional(), Length(1, 64)])
    link = StringField('Link', validators=[Optional(), Length(1, 64)])

    imagem        = FileField(u'Imagem')
    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class MarcaUploadForm(FlaskForm):
    link = StringField('Link', validators=[Optional(), Length(1, 64)])
    marca        = FileField(u'Marca')
    enviar = SubmitField('Salvar')
    descartar = SubmitField('Cancelar')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class FotoUploadForm(FlaskForm):
    banner        = FileField(u'Banner')
    enviar = SubmitField('Salvar')
    descartar = SubmitField('Cancelar')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)