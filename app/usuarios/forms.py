from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, PasswordField, BooleanField, DateTimeField, IntegerField, RadioField, SelectField, FormField, FloatField, FileField
from wtforms.validators import Optional, Length, Required, DataRequired, URL

class bancoForm(FlaskForm):
    banco        = FileField(u'Arquivo do banco')
    
    salvar = SubmitField("Enviar")
    
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class acessoForm(FlaskForm):
    acesso = BooleanField(u'Tem acesso ao sistema?')
    perfilUsuario = SelectField('Perfil de usuário', choices=[])
    cadCliente = BooleanField(u'Cadastro Clientes')
    cadFornecedor = BooleanField(u'Cadastro fornecedor')
    cadEstoque = BooleanField(u'Cadastro estoque')
    cadPedidos = BooleanField(u'Pedidos')
    cadOrcamentos = BooleanField(u'Orçamentos')
    cadContasPagar = BooleanField(u'Contas a pagar')
    cadContasReceber = BooleanField(u'Contas a receber')
    cadFuncionarios = BooleanField(u'Funcionários')
    cadConfig = BooleanField(u'Configurações')

    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")

class FuncionarioForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[Optional(), Length(1, 64)])
    perfilUsuario = SelectField('Perfil de usuário', choices=[])

    tipoFuncionario = SelectField(u'Tipo de funcionario', choices=[('Contrato', 'Contrato'), ('CLT', 'CLT'), ('Temporario', 'Temporario'), ('Estagio', 'Estagio')])
    cpf = StringField('CPF', validators=[Optional(), Length(1, 64)])
    frete = StringField('Frete', validators=[Optional(), Length(1, 64)])
    RegGer  = StringField('RG', validators=[Optional(), Length(1, 64)])
    estadoCivil = SelectField(u'Estado Civil', choices=[('Casado(a)', 'Casado(a)'), ('Solteiro(a)', 'Solteiro(a)'), ('Divorciado(a)', 'Divorciado(a)'), ('Viuvo(a)', 'Viuvo(a)')])
    genero = SelectField(u'Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')])
    dataNascimento = DateTimeField('Data de Nascimento', format='%d/%m/%Y')
    nacionalidade = SelectField(u'Nacionalidade', choices=[('Brasileiro', 'Brasileiro')])
    naturalidade = SelectField(u'Naturalidade', choices=[('Porto Alegre', 'Porto Alegre')])
    observacoes = TextAreaField('Observação')


    UF = SelectField(u'Unidade Federativa(UF)', choices=[('RS', 'RS')])
    municipio = SelectField(u'Município', choices=[('Porto Alegre', 'Porto Alegre')])
    pais = SelectField(u'País', choices=[('Brasil', 'Brasil')])
    CEP = StringField('CEP', validators=[Optional(), Length(1, 64)])
    endereco = StringField('Endereço', validators=[Optional(), Length(1, 64)])
    numero = IntegerField('Numero')
    complemento = StringField('Complemento', validators=[Optional(), Length(1, 64)])
    bairro = StringField('Bairro', validators=[Optional(), Length(1, 64)])

    telefone = StringField('Telefone Fixo', validators=[Optional(), Length(1, 64)])
    celular = StringField('Celular', validators=[Optional(), Length(1, 64)])    
    whatsapp = StringField('WhatsApp', validators=[Optional(), Length(1, 64)])  
    linkedin = StringField('Linkedin', validators=[Optional(), Length(1, 64)])    
    facebook = StringField('Facebook', validators=[Optional(), Length(1, 64)])  
    instagram = StringField('Instagram', validators=[Optional(), Length(1, 64)])
    twitter = StringField('Twitter', validators=[Optional(), Length(1, 64)])
    email = StringField('Email principal', validators=[Optional(), Length(1, 64)])
    email2 = StringField('Email secundário', validators=[Optional(), Length(1, 64)])

    cargo = SelectField(u'Cargo', choices=[])
    salarioBruto =  StringField('Salario Bruto', validators=[Optional(), Length(1, 64)])
    descontoINSS =  StringField('Desconto INSS', validators=[Optional(), Length(1, 64)])
    salarioLiquido =  StringField('Salario Liquido', validators=[Optional(), Length(1, 64)])

    imagem        = FileField(u'Foto do funcionario')
    
    senha = PasswordField('Senha')
    confirmarSenha = PasswordField('Confirmar senha')
    
    salvar = SubmitField("Salvar")
    cancelar = SubmitField("Cancelar")
    
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

class excluirForm(FlaskForm):
    s = SubmitField("Sim")
    n = SubmitField("Não")

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


        
class viewForm(FlaskForm):
   viewFormfuncionario = BooleanField('funcionario')
   viewFormtipoFuncionario = BooleanField('tipoFuncionario')
   viewFormCPF = BooleanField('CPF')
   viewFormRegGer = BooleanField('RegGer')
   viewFormestadoCivil = BooleanField('estadoCivil')
   viewFormgenero = BooleanField('genero')
   viewFormdataNascimento = BooleanField('Data de Nascimento')
   viewFormnacionalidade = BooleanField('nacionalidade')
   viewFormnaturalidade = BooleanField('naturalidade')
   viewFormimagem = BooleanField('Imagem')

   viewFormUF = BooleanField('UF')
   viewFormmunicipio = BooleanField('municipio')
   viewFormpais = BooleanField('pais')
   viewFormCEP = BooleanField('CEP')
   viewFormendereco = BooleanField('endereco')
   viewFormnumero = BooleanField('numero')
   viewFormcomplemento = BooleanField('complemento')
   viewFormbairro = BooleanField('bairro')

   viewFormtelefone = BooleanField('telefone')
   viewFormcelular = BooleanField('celular')
   viewFormwhatsapp = BooleanField('whatsapp')
   viewFormlinkedin = BooleanField('linkedin')
   viewFormfacebook = BooleanField('facebook')
   viewForminstagram = BooleanField('instagram')
   viewFormtwitter = BooleanField('twitter')
   viewFormemail = BooleanField('email')
   viewFormemail2 = BooleanField('email2')

   viewFormcargo = BooleanField('cargo')
   viewFormsalarioBruto = BooleanField('salarioBruto')
   viewFormdescontoINSS = BooleanField('descontoINSS')
   viewFormsalarioLiquido = BooleanField('salarioLiquido')
   viewFormacesso = BooleanField('acesso')
   viewFormtipoAcesso = BooleanField('tipoAcesso')

   salvar = SubmitField('Salvar')
   cancelar = SubmitField('Cancelar')
    