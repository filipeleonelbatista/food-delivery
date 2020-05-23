from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField, BooleanField, IntegerField, DateField, DateTimeField, PasswordField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class inicioForm(FlaskForm):
    vamos = SubmitField("Vamos nessa!")

class usuarioForm(FlaskForm):
    funcionario = StringField('Nome do usuário', validators=[Optional(), Length(1, 64)])
    cpf = StringField('CPF', validators=[Optional(), Length(1, 64)])
    dataNascimento = DateField('Data de Nacimento', format="%d/%m/%Y")

    UF = SelectField(u'Unidade Federativa(UF)', choices=[('RS', 'RS')])
    municipio = SelectField(u'Município', choices=[('Porto Alegre', 'Porto Alegre')])
    pais = SelectField(u'País', choices=[('Brasil', 'Brasil')])
    CEP = StringField('CEP', render_kw={"placeholder": "Digite seu CEP"}, validators=[Optional(), Length(1, 64)])
    endereco = StringField('Endereço', render_kw={"placeholder": "Digite a Rua"}, validators=[Optional(), Length(1, 64)])
    numero = IntegerField('Numero', render_kw={"placeholder": "Digite o numero do local"})
    complemento = StringField('Complemento', render_kw={"placeholder": "Complemento"}, validators=[Optional(), Length(1, 64)])
    bairro = StringField('Bairro', render_kw={"placeholder": "Digite seu Bairro"}, validators=[Optional(), Length(1, 64)])


    telefone = StringField('Telefone Fixo', render_kw={"placeholder": "Telefone Fixo"}, validators=[Optional(), Length(1, 64)])
    celular = StringField('Celular', render_kw={"placeholder": "Celular"}, validators=[Optional(), Length(1, 64)])    
    email = StringField('Email principal', render_kw={"placeholder": "Email Principal"}, validators=[Optional(), Length(1, 64)])
   
    senha = PasswordField('Senha', render_kw={"placeholder": "Digite uma senha"})
    confirmarSenha = PasswordField('Confirmar senha', render_kw={"placeholder": "Digite novamente a senha"})
    
    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")

class FotoUploadForm(FlaskForm):
    logo        = FileField(u'Image File')
    icon        = FileField(u'Image File')
    user        = FileField(u'Image File')
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

class cadastroForm(FlaskForm):
    razaoSocial = StringField('Razão Social', render_kw={"placeholder": "Razão Social"}, validators=[Optional(), Length(1, 64)])
    nomeFantasia = StringField('Nome Fantasia', render_kw={"placeholder": "Nome Fantasia"}, validators=[Optional(), Length(1, 64)])
    nomeContato = StringField('nomeContato', render_kw={"placeholder": "Digite seu Nome"}, validators=[Optional(), Length(1, 64)])
    CPF = StringField('CPF', render_kw={"placeholder": "Digite seu CPF"},  validators=[Optional(), Length(1, 64)])
    RegGer = StringField('RG', render_kw={"placeholder": "Digite seu RG"},  validators=[Optional(), Length(1, 64)])
    CNPJ = StringField('CNPJ', render_kw={"placeholder": "Digite seu CNPJ"}, validators=[Optional(), Length(1, 64)])
    InscEst = StringField('InscEst', render_kw={"placeholder": "Digite sua Inscrição Estadual"}, validators=[Optional(), Length(1, 64)])
    InscMun = StringField('InscMun', render_kw={"placeholder": "Digite sua Inscrição Municipal"}, validators=[Optional(), Length(1, 64)])
    imprimir = BooleanField('Imprimir automaticamente os pedidos após criação?')
    tipoImpressao = BooleanField('Imprimir em impressora termica?')

# Informações da loja virtual
    whatsapp = StringField('Whatsapp', render_kw={"placeholder": "Digite seu WhatsApp"}, validators=[Optional(), Length(1, 64)])
    facebook = StringField('Facebook', render_kw={"placeholder": "Digite seu Facebook"}, validators=[Optional(), Length(1, 64)])
    facebookPgId = StringField('FacebookPgId', render_kw={"placeholder": "Digite seu Facebook PageId"}, validators=[Optional(), Length(1, 64)])
    twitter = StringField('Twitter', render_kw={"placeholder": "Digite seu Twitter"}, validators=[Optional(), Length(1, 64)])
    instagram = StringField('Instagram', render_kw={"placeholder": "Digite seu Instagram"}, validators=[Optional(), Length(1, 64)])
    youtube = StringField('Youtube', render_kw={"placeholder": "Digite seu canal no Youtube"}, validators=[Optional(), Length(1, 64)])
    linkedin = StringField('Linkedin', render_kw={"placeholder": "Digite seu Linkedin"}, validators=[Optional(), Length(1, 64)])
    telefone = StringField('Telefone', render_kw={"placeholder": "Digite seu Telefone"}, validators=[Optional(), Length(1, 64)])
    descricao = TextAreaField('Descricao', render_kw={"placeholder": "Digite ume breve descrição sobre sua empresa"})
    sobre = TextAreaField('Sobre a empresa', render_kw={"placeholder": "Conte-nos sua história..."})
    email = StringField('Email', render_kw={"placeholder": "Digite seu Email"}, validators=[Optional(), Length(1, 64)])

#  identificação visual
    logo        = FileField(u'Logotipo')
    icon        = FileField(u'Icone')
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

    logoNome = BooleanField('logoNome')

#  Localização
    UF = SelectField(u'Unidade Federativa(UF)', choices=[('RS', 'RS')])
    municipio = SelectField(u'Município', choices=[('Porto Alegre', 'Porto Alegre')])
    pais = SelectField(u'País', choices=[('Brasil', 'Brasil')])
    CEP = StringField('CEP', render_kw={"placeholder": "Digite seu CEP"}, validators=[Optional(), Length(1, 64)])
    endereco = StringField('Endereço', render_kw={"placeholder": "Digite a Rua"}, validators=[Optional(), Length(1, 64)])
    numero = IntegerField('Numero', render_kw={"placeholder": "Digite o numero do local"})
    complemento = StringField('Complemento', render_kw={"placeholder": "Complemento"}, validators=[Optional(), Length(1, 64)])
    bairro = StringField('Bairro', render_kw={"placeholder": "Digite seu Bairro"}, validators=[Optional(), Length(1, 64)])

# Exibir na pagina
    mostrarFloat = BooleanField('mostrarFloat')
    mostrarWp = BooleanField('mostrarWp')
    mostrarFb = BooleanField('mostrarFb')
    mostrarTw = BooleanField('mostrarTw')
    mostrarIn = BooleanField('mostrarIn')
    mostrarYt = BooleanField('mostrarYt')
    mostrarLn = BooleanField('mostrarLn')
    mostrarTe = BooleanField('mostrarTe')

    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")


def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)


 