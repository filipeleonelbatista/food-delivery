import hashlib
from datetime import datetime

from flask import request

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Mensagens(db.Model):    
    __tablename__ = 'mensagens'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    remetente = db.Column(db.String(64))
    destinatario = db.Column(db.String(64))
    dataEnvio = db.Column(db.DateTime())
    dataLeitura = db.Column(db.DateTime())
    mensagem = db.Column(db.String(255))
    imagemMsg = db.Column(db.String(64))
    status = db.Column(db.Integer)
    pasta = db.Column(db.String(64))

class Banner(db.Model):    
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ordem = db.Column(db.Integer) 
    nome = db.Column(db.String(64))

class perfilUsuario(db.Model):    
    __tablename__ = 'perfilUsuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(64))
    cor = db.Column(db.String(64))

class status(db.Model):    
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    ordem = db.Column(db.Integer) 
    nome = db.Column(db.String(64))
    cor = db.Column(db.String(64))

class config(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True) 
    versao = db.Column(db.String(64))

    #  Informações legais da empresa
    razaoSocial = db.Column(db.String(64))
    nomeFantasia = db.Column(db.String(64))
    CNPJ = db.Column(db.String(64))
    imprimir = db.Column(db.Boolean, default=True)
    tipoImpressao = db.Column(db.Boolean, default=True)
    ativa = db.Column(db.Boolean, default=True)    
    validade = db.Column(db.DateTime())

    # status padrão
    id_statusPadrao_aberto = db.Column(db.Integer)
    id_statusPadrao_cozinha = db.Column(db.Integer)
    id_statusPadrao_entrega = db.Column(db.Integer)
    id_statusPadrao_finalizado = db.Column(db.Integer)

    
    mensagensSaida = db.Column(db.Boolean, default=True)    


    update = db.Column(db.Boolean, default=True)
    sobreUpdate = db.Column(db.String(255))


    # Informações da loja virtual
    whatsapp = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    facebook = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    facebookPgId = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    twitter = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    instagram = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    youtube = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    linkedin = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    telefone = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    descricao = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")
    sobre = db.Column(db.String(255), default="<SEM INFORMAÇÃO>")
    email = db.Column(db.String(64), default="<SEM INFORMAÇÃO>")

    #  identificação visual
    
    icon = db.Column(db.String(64), default="default-favicon.png")    
    logo = db.Column(db.String(64), default="default-logo.png")

    #  Localização
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'), default=1)    
    endereco = db.relationship("endereco")

class endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    uf = db.Column(db.String(64), nullable=False, default='RS')
    municipio = db.Column(db.String(64), nullable=False, default='Gravataí')
    pais = db.Column(db.String(64), nullable=False, default='Brasil')
    cep = db.Column(db.String(64), default="94170-244")
    endereco  = db.Column(db.String(64), nullable=False, default='Rua um')
    numero  = db.Column(db.Integer, default=123)
    complemento = db.Column(db.String(64), default='Casa da frente')
    bairro = db.Column(db.String(64), nullable=False, default='Bairro Novo')

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    categoria = db.Column(db.String(64))

class Estoque(db.Model):
    __tablename__ = 'estoque'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nomeProduto = db.Column(db.String(64))
    descricaoProduto = db.Column(db.String(64))
    precoVenda = db.Column(db.String(64))
    imagem = db.Column(db.String(64))    
    exibirSite = db.Column(db.Boolean, default=True)
    
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), default=1)
    categoria = db.relationship("Categoria")

class View(db.Model):
    __tablename__ = 'view'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    CPFView = db.Column(db.Boolean, default=True)
    imagemView = db.Column(db.Boolean, default=True)
    is_adminView = db.Column(db.Boolean, default=True)
    password_hashView = db.Column(db.Boolean, default=False)
    nomeView = db.Column(db.Boolean, default=True)
    telefoneView = db.Column(db.Boolean, default=False)
    celularView = db.Column(db.Boolean, default=False)
    emailView = db.Column(db.Boolean, default=True)
    UFView = db.Column(db.Boolean, default=False)
    municipioView = db.Column(db.Boolean, default=True)
    paisView = db.Column(db.Boolean, default=False)
    CEPView = db.Column(db.Boolean, default=False)
    enderecoView = db.Column(db.Boolean, default=True)
    numeroView = db.Column(db.Boolean, default=True)
    complementoView = db.Column(db.Boolean, default=False)
    bairroView = db.Column(db.Boolean, default=True)

class InicioView(db.Model):
    __tablename__ = 'inicioview'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cliente = db.Column(db.Boolean, default=True)
    funcionario = db.Column(db.Boolean, default=True)
    pedido = db.Column(db.Boolean, default=True)
    estoque = db.Column(db.Boolean, default=True)
    graficoPedidos = db.Column(db.Boolean, default=True)

class Cliente(UserMixin, db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(64), nullable=False)
    CPF = db.Column(db.String(64), nullable=False, unique=True)
    dataNascimento = db.Column(db.DateTime())
    password_hash = db.Column(db.String(256))

    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))
    endereco = db.relationship("endereco")

    telefone = db.Column(db.String(64))
    celular = db.Column(db.String(64))
    email = db.Column(db.String(64))
    frete = db.Column(db.String(64))

    imagem = db.Column(db.String(64))
    observacoes = db.Column(db.Text)    

    id_perfilUsuario = db.Column(db.Integer, db.ForeignKey('perfilUsuario.id'))
    perfilUsuario = db.relationship("perfilUsuario")

    id_view = db.Column(db.Integer, db.ForeignKey('view.id'))
    view = db.relationship("View")   

    id_inicioview = db.Column(db.Integer, db.ForeignKey('inicioview.id'), default=1)
    inicioview = db.relationship("InicioView")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def createUsername(self, password):
        self.username = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(64), nullable=False)
    CPF = db.Column(db.String(64), nullable=False, unique=True)
    dataNascimento = db.Column(db.DateTime())
    password_hash = db.Column(db.String(256))

    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id'))
    endereco = db.relationship("endereco")

    telefone = db.Column(db.String(64))
    celular = db.Column(db.String(64))
    email = db.Column(db.String(64))
    frete = db.Column(db.String(64))

    imagem = db.Column(db.String(64))
    observacoes = db.Column(db.Text)    

    id_perfilUsuario = db.Column(db.Integer, db.ForeignKey('perfilUsuario.id'))
    perfilUsuario = db.relationship("perfilUsuario")

    id_view = db.Column(db.Integer, db.ForeignKey('view.id'))
    view = db.relationship("View")   

    id_inicioview = db.Column(db.Integer, db.ForeignKey('inicioview.id'), default=1)
    inicioview = db.relationship("InicioView")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def createUsername(self, password):
        self.username = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id'), default=1)
    pedido = db.relationship("Pedido")
    quantidade = db.Column(db.String(64))
    produto = db.Column(db.String(64))
    precoUnitario = db.Column(db.String(64))    
    precoTotal = db.Column(db.String(64))  
    
    id_estoque = db.Column(db.Integer, db.ForeignKey('estoque.id'), default=1)
    estoque = db.relationship("Estoque")

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    dtCreate = db.Column(db.DateTime())
    dtUpdate = db.Column(db.DateTime())
    subtotal = db.Column(db.String(64))
    desconto = db.Column(db.String(64))
    frete = db.Column(db.String(64))    
    total = db.Column(db.String(64))  
    formaPagamento = db.Column(db.String(64))      
    observacao = db.Column(db.String(64))   
    
    entrega = db.Column(db.Boolean, default=True)
    
    id_responsavel = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
    responsavel = db.relationship("Usuario")
    
    id_cliente = db.Column(db.Integer, db.ForeignKey('Cliente.id'))
    cliente = db.relationship("Cliente")
    
    id_entregador = db.Column(db.String(64)) 

    id_status = db.Column(db.Integer, db.ForeignKey('status.id'))
    status = db.relationship("status")