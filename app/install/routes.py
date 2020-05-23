import os
from random import randint
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from pyUFbr.baseuf import ufbr

from datetime import datetime

from app import db
from app.install.forms import cadastroForm, usuarioForm, FotoUploadForm, inicioForm
from . import install
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, Categoria, perfilUsuario, status

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

import os
if os.name == 'nt':
    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
else:
    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@install.route('/install', methods=['GET', 'POST'])
def index():
    form = inicioForm()
    if form.vamos.data == True and request.method == 'POST':
        
        db.create_all()
        try:            
            perfil = perfilUsuario(
                nome = "Superadministrador",
                cor = "success"
            )     
            db.session.add(perfil) 
            perfil = perfilUsuario(
                nome = "Administrador",
                cor = "success"
            )     
            db.session.add(perfil) 
            perfil = perfilUsuario(
                nome = "Vendedor",
                cor = "primary"
            )     
            db.session.add(perfil) 
            perfil = perfilUsuario(
                nome = "Entregador",
                cor = "warning"
            )     
            db.session.add(perfil)  
            perfil = perfilUsuario(
                nome = "Cosinha",
                cor = "warning"
            )     
            db.session.add(perfil)  
            perfil = perfilUsuario(
                nome = "Cliente",
                cor = "info"
            )     
            db.session.add(perfil)          
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar algum perfil de usuario","danger")
        try:            
            Status = status(
                ordem = 0,
                nome = "Aguardando Confirmação",
                cor = "warning"
            )     
            db.session.add(Status)
            Status = status(
                ordem = 1,
                nome = "Aberto",
                cor = "primary"
            )     
            db.session.add(Status)
            Status = status(
                ordem = 2,
                nome = "Em produção",
                cor = "warning"
            )     
            db.session.add(Status)
            Status = status(
                ordem = 3,
                nome = "Saiu para entrega",
                cor = "warning"
            )     
            db.session.add(Status)
            Status = status(
                ordem = 4,
                nome = "Finalizado",
                cor = "success"
            )     
            db.session.add(Status)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar algum status","danger")
        try:            
            cat = Categoria(
                categoria = "Padrão"
            )     
            db.session.add(cat)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar categoria","danger")
        # definindo usuario default
        try:            
            Endereco = endereco(
                uf = "RS",
                municipio = "Gravataí",
                pais = "Brasil",
                cep = "94170-244",
                endereco = "Tv. Itacolomi Dois",
                numero = "343",
                complemento = "<vazio>",
                bairro = "Santa Cruz"
            )     
            db.session.add(Endereco)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar endereço","danger")
        try:            
            view = View(
                CPFView = True,
                imagemView = True,
                is_adminView = True,
                password_hashView = False,
                nomeView = True,
                telefoneView = False,
                celularView = False,
                emailView = True,
                UFView = False,
                municipioView = True,
                paisView = False,
                CEPView = False,
                enderecoView = True,
                numeroView = True,
                complementoView = False,
                bairroView = True
            )     
            db.session.add(view)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar View","danger")
        try:            
            Inicioview = InicioView(
                cliente = True,
                funcionario = True,
                pedido = True,
                estoque = True,
                graficoPedidos = True
            )     
            db.session.add(Inicioview)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar clienteView","danger")
        try:      
            user = Usuario(
                nome = "Administrador",
                CPF = "111.111.111-11",
                dataNascimento = datetime.strptime("11/01/1994","%d/%m/%Y"),
                password = "11111111111admin",
                id_endereco = Endereco.id,  

                telefone = "(51) 3128-1659",
                celular = "(51) 99290-4780",
                email = "administrador@leonelinformatica.com.br",
                frete = "0.00",
                imagem = "default-admin.jpg",
                observacoes = "Administrador do Sistema",

                id_perfilUsuario = 1,
                id_view = view.id,              
                id_inicioview  = Inicioview.id
            )     
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar usuario padrão","danger")

        flash("Banco criado com sucesso","success")
        return redirect(url_for('install.index1'))

    return render_template('install/index.html',
                            form = form
                            )


@install.route('/dadosdoproprietario', methods=['GET', 'POST'])
def index1():   
    form = usuarioForm() 

    form.UF.choices = [('RS', 'RS')]
    for valor in ufbr.list_uf:
        form.UF.choices += [(valor, valor)]
    form.municipio.choices = [('Selecione uma opção', 'Selecione uma opção')]
    for valor in ufbr.list_cidades('RS'):
        form.municipio.choices += [(valor, valor)]

    if form.salvar.data == True and request.method == 'POST':
        novaSenha = form.cpf.data.replace('.','').replace('-','')
        try:            
            Endereco = endereco(
                uf = form.UF.data,
                municipio = form.municipio.data,
                pais = form.pais.data,
                cep = form.CEP.data,
                endereco = form.endereco.data,
                numero = form.numero.data,
                complemento = form.complemento.data,
                bairro = form.bairro.data
            )     
            db.session.add(Endereco)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar endereço","danger")
        try:            
            view = View(
                CPFView = True,
                imagemView = True,
                is_adminView = True,
                password_hashView = False,
                nomeView = True,
                telefoneView = False,
                celularView = False,
                emailView = True,
                UFView = False,
                municipioView = True,
                paisView = False,
                CEPView = False,
                enderecoView = True,
                numeroView = True,
                complementoView = False,
                bairroView = True
            )     
            db.session.add(view)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar View","danger")
        try:            
            Inicioview = InicioView(
                cliente = True,
                funcionario = True,
                pedido = True,
                estoque = True,
                graficoPedidos = True
            )     
            db.session.add(Inicioview)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar inicioView","danger")
        try:
            funcionario =  Usuario(
                
                nome = form.funcionario.data,
                CPF = form.cpf.data,
                dataNascimento = form.dataNascimento.data,
                password = novaSenha,
                id_endereco = Endereco.id,  

                telefone = form.telefone.data,
                celular = form.celular.data,
                email = form.email.data,
                frete = "0.00",
                imagem = "default-user.jpg",
                observacoes = "Administrador da empresa",

                id_perfilUsuario = 2,
                id_view = view.id,              
                id_inicioview  = Inicioview.id
            )
            db.session.add(funcionario)
            db.session.commit()
            flash("Usuário cadastrado com sucesso","success")
            return redirect(url_for('install.index2'))
        except:
            db.session.rollback()
            flash("Algo deu errado","danger")

    return render_template('install/index1.html', 
                            form=form
                            )

@install.route('/dadosempresa', methods=['GET', 'POST'])
def index2():   
    form = cadastroForm() 
    controle = 0

    usuario = Usuario.query.filter_by(id=2).first()
    
    form.endereco.data = usuario.endereco.endereco
    form.numero.data = usuario.endereco.numero
    form.complemento.data = usuario.endereco.complemento
    form.bairro.data = usuario.endereco.bairro
    form.pais.data = usuario.endereco.pais
    form.CEP.data = usuario.endereco.cep

    form.UF.choices = [( usuario.endereco.uf,  usuario.endereco.uf)]
    for valor in ufbr.list_uf:
        form.UF.choices += [(valor, valor)]
    form.municipio.choices = [(usuario.endereco.municipio, usuario.endereco.municipio), ('Selecione uma opção', 'Selecione uma opção')]
    for valor in ufbr.list_cidades( usuario.endereco.uf):
        form.municipio.choices += [(valor, valor)]

    if form.salvar.data == True and request.method == 'POST':
       
        # Inserir o upload aqui
        if 'icon' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['icon']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    icone = 'default-favicon.png'

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                arquivo = newfilename
        else:
            icone = 'default-favicon.png'
        
        # Inserir o upload aqui
        if 'logo' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['logo']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    logo = 'default-logo.png'

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                arquivo = newfilename
        else:
            logo = 'default-logo.png'
        

        try:            
            Endereco = endereco(
                uf = form.UF.data,
                municipio = form.municipio.data,
                pais = form.pais.data,
                cep = form.CEP.data,
                endereco = form.endereco.data,
                numero = form.numero.data,
                complemento = form.complemento.data,
                bairro = form.bairro.data
            )     
            db.session.add(Endereco)
            db.session.commit()
        except:
            db.session.rollback()
            flash("Erro ao adicionar endereço","danger")
       
        
        mes = 0
        validadeNova = datetime.now()
        if validadeNova.month == 12:
            mes = 1
        else:
            mes = validadeNova.month + 1

        try:
            Config =  config(
                razaoSocial = form.razaoSocial.data,
                nomeFantasia = form.nomeFantasia.data,
                CNPJ = form.CNPJ.data,
                imprimir = form.imprimir.data,
                tipoImpressao = form.tipoImpressao.data,

                versao = '2.021.92',

                mensagensSaida = True,
                
                ativa = True,
                validade = datetime.strptime(str(validadeNova.day)+"/"+str(mes)+"/"+str(validadeNova.year),"%d/%m/%Y"),
                
                whatsapp = form.whatsapp.data,
                facebook = form.facebook.data,
                twitter = form.twitter.data,
                instagram = form.instagram.data,
                youtube = form.youtube.data,
                linkedin = form.linkedin.data,
                telefone = form.telefone.data,
                descricao = form.descricao.data,
                sobre = form.sobre.data,
                email = form.email.data,

                icon = icone,
                logo = logo,
                
                id_endereco = Endereco.id
            )
            db.session.add(Config)
            db.session.commit()
            flash("Configurações cadastrado com sucesso","success")
            return redirect(url_for('install.index3'))
        except:
            db.session.rollback()
            flash("Algo deu errado","danger")


    return render_template('install/index2.html', 
                            form=form, 
                            )

@install.route('/pronto', methods=['GET', 'POST'])
def index3():
    return render_template('install/index3.html')
