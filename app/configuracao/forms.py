from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, PasswordField, BooleanField, DateTimeField, IntegerField, RadioField, SelectField, FormField, FloatField, FileField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class excluirForm(FlaskForm):
    s = SubmitField("Sim")
    n = SubmitField("Não")

class statusForm(FlaskForm):
    nome = StringField('Nome do status', render_kw={"placeholder": "Nome do status"}, validators=[Optional(), Length(1, 64)])
    cor = StringField('Cor', render_kw={"placeholder": "Cor"}, validators=[Optional(), Length(1, 64)])
    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")
    
class cargoForm(FlaskForm):   
    cargo = StringField('Cargo', validators=[Optional(), Length(1, 64)])
    acesso = BooleanField(u'Tem acesso ao sistema?')
    cadCliente = BooleanField(u'Cadastro Clientes')
    cadFornecedor = BooleanField(u'Cadastro fornecedor')
    cadEstoque = BooleanField(u'Cadastro estoque')
    cadPedidos = BooleanField(u'Pedidos')
    cadOrcamentos = BooleanField(u'Orçamentos')
    cadContasPagar = BooleanField(u'Contas a pagar')
    cadContasReceber = BooleanField(u'Contas a receber')
    cadFuncionarios = BooleanField(u'Funcionários')
    cadConfig = BooleanField(u'Configurações')
    salvar = SubmitField('Salvar')
    cancelar = SubmitField('Cancelar')

class empresaForm(FlaskForm):   
    razaoSocial = StringField('Razão Social', render_kw={"placeholder": "Razão Social"}, validators=[Optional(), Length(1, 64)])
    nomeFantasia = StringField('Nome Fantasia', render_kw={"placeholder": "Nome Fantasia"}, validators=[Optional(), Length(1, 64)])
    nomeContato = StringField('Nome', render_kw={"placeholder": "Digite seu Nome"}, validators=[Optional(), Length(1, 64)])
    CPF = StringField('CPF/CNPJ', render_kw={"placeholder": "Digite seu CPF"},  validators=[Optional(), Length(1, 64)])
    RegGer = StringField('RG', render_kw={"placeholder": "Digite seu RG"},  validators=[Optional(), Length(1, 64)])
    CNPJ = StringField('CNPJ', render_kw={"placeholder": "Digite seu CNPJ"}, validators=[Optional(), Length(1, 64)])
    InscEst = StringField('Inscrição Estadual', render_kw={"placeholder": "Digite sua Inscrição Estadual"}, validators=[Optional(), Length(1, 64)])
    InscMun = StringField('Inscrição Municipal', render_kw={"placeholder": "Digite sua Inscrição Municipal"}, validators=[Optional(), Length(1, 64)])
    imprimir = BooleanField('Imprimir automaticamente os pedidos?')
    imprimirTermica = BooleanField('Imprimir em impressora termica?')
    ativo = BooleanField('Sistema ativado?')
    update = BooleanField('Possui atualização?')

# Informações da loja virtual
    whatsapp = StringField('WhatsApp', render_kw={"placeholder": "Digite seu WhatsApp"}, validators=[Optional(), Length(1, 64)])
    facebook = StringField('Facebook', render_kw={"placeholder": "Digite seu Facebook"}, validators=[Optional(), Length(1, 64)])
    facebookPgId = StringField('Facebook PageId', render_kw={"placeholder": "Digite seu Facebook PageId"}, validators=[Optional(), Length(1, 64)])
    twitter = StringField('Twitter', render_kw={"placeholder": "Digite seu Twitter"}, validators=[Optional(), Length(1, 64)])
    instagram = StringField('Instagram', render_kw={"placeholder": "Digite seu Instagram"}, validators=[Optional(), Length(1, 64)])
    youtube = StringField('Youtube', render_kw={"placeholder": "Digite seu canal no Youtube"}, validators=[Optional(), Length(1, 64)])
    linkedin = StringField('Linkedin', render_kw={"placeholder": "Digite seu Linkedin"}, validators=[Optional(), Length(1, 64)])
    telefone = StringField('Telefone', render_kw={"placeholder": "Digite seu Telefone"}, validators=[Optional(), Length(1, 64)])
    descricao = TextAreaField('Descrição curta', render_kw={"placeholder": "Digite ume breve descrição sobre sua empresa"})
    sobre = TextAreaField('Sobre a empresa', render_kw={"placeholder": "Conte-nos sua história..."})
    sobreUpdate = TextAreaField('Sobre a atualização', render_kw={"placeholder": "Informações da atualização"})
    email = StringField('email', render_kw={"placeholder": "Digite seu Email"}, validators=[Optional(), Length(1, 64)])

#  identificação visual
    fotoEmpresa        = FileField(u'Foto da empresa')
    logo        = FileField(u'Logotipo')
    icon        = FileField(u'Icone')
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

#  Localização
    UF = SelectField(u'Unidade Federativa(UF)', choices=[])
    municipio = SelectField(u'Município', choices=[])
    pais = SelectField(u'País', choices=[])
    CEP = StringField('CEP', render_kw={"placeholder": "Digite seu CEP"}, validators=[Optional(), Length(1, 64)])
    endereco = StringField('Endereço', render_kw={"placeholder": "Digite a Rua"}, validators=[Optional(), Length(1, 64)])
    numero = IntegerField('Numero', render_kw={"placeholder": "Digite o numero do local"})
    complemento = StringField('Complemento', render_kw={"placeholder": "Complemento"}, validators=[Optional(), Length(1, 64)])
    bairro = StringField('Bairro', render_kw={"placeholder": "Digite seu Bairro"}, validators=[Optional(), Length(1, 64)])

# Exibir na pagina
    mostrarFloat = BooleanField('Mostrar botão flutuante')
    mostrarWp = BooleanField('Mostrar Whatsapp')
    mostrarFb = BooleanField('Mostrar Facebook')
    mostrarTw = BooleanField('Mostrar Twitter')
    mostrarIn = BooleanField('Mostrar Instagram')
    mostrarYt = BooleanField('Mostrar Youtube')
    mostrarLn = BooleanField('Mostrar Linkedin')
    mostrarTe = BooleanField('Mostrar Telefone')

    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")

def upload(request):
    form = UploadForm(request.POST)
    if form.image.data:
        image_data = request.FILES[form.image.name].read()
        open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)


 