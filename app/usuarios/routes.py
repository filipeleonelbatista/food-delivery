import os
from random import randint
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user

from pyUFbr.baseuf import ufbr

from datetime import datetime

from app import db
from app.usuarios.forms import bancoForm, FuncionarioForm, FotoUploadForm, excluirForm, viewForm, acessoForm
from . import usuarios
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Cliente, Item, Pedido, Categoria, perfilUsuario

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'sql'])

import os
if os.name == 'nt':
    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
else:
    UPLOAD_FOLDER = os.getcwd()+'/app/static/images/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@usuarios.route('/clientes', methods=['GET', 'POST'])
@login_required
def clientes():
    funcionarios = Cliente.query.filter_by(id_perfilUsuario = 6).all()
    view = View.query.filter_by(id = current_user.id_view).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('usuarios/clientes/clientes.html', 
                            funcionarios = funcionarios, 
                            view = view,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
@usuarios.route('/clientes/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrarCliente():
    controle = 0
    funcionarioForm = FuncionarioForm()

    perfil = perfilUsuario.query.all()
    for perf in perfil: 
        if perf.id == 6:       
            funcionarioForm.perfilUsuario.choices += [(perf.id, perf.nome)]
            

    funcionarioForm.UF.choices = [('RS', 'RS')]
    for valor in ufbr.list_uf:
        funcionarioForm.UF.choices += [(valor, valor)]
    funcionarioForm.municipio.choices = [('Selecione uma opção', 'Selecione uma opção')]
    for valor in ufbr.list_cidades('RS'):
        funcionarioForm.municipio.choices += [(valor, valor)]

    if funcionarioForm.cancelar.data == True and request.method == 'POST':
        return redirect(url_for('usuarios.clientes'))

    if funcionarioForm.salvar.data == True and request.method == 'POST':
        # Seta a senha padrão o cpf sem caracteres especiais
        novaSenha = funcionarioForm.cpf.data.replace('.','').replace('-','')
        try:
            Endereco = endereco(
                uf = funcionarioForm.UF.data,
                municipio = funcionarioForm.municipio.data,
                pais = funcionarioForm.pais.data,
                cep = funcionarioForm.CEP.data,
                endereco = funcionarioForm.endereco.data,
                numero = funcionarioForm.numero.data,
                complemento = funcionarioForm.complemento.data,
                bairro = funcionarioForm.bairro.data
            )
            db.session.add(Endereco)            
            db.session.commit()
            # flash('Endereço Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar endereço', 'danger')

        # ADICIONANDO AS VIEWS DO FUNCIONARIO 
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
            # flash('View Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar View', 'danger')
        try:
            inicio = InicioView(
                cliente = True,
                funcionario = True,
                pedido = True,
                estoque = True,
                graficoPedidos = True
            )            
            db.session.add(inicio)            
            db.session.commit()
            # flash('View Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar View', 'danger')
        # Finalizando a criação das views

        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = 'default-user.jpg'

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
            arquivo = 'default-user.jpg'
        try:            
            funcionario = Cliente(
                nome = funcionarioForm.nome.data,
                CPF = funcionarioForm.cpf.data,
                dataNascimento = funcionarioForm.dataNascimento.data,
                password = novaSenha,
                imagem =  arquivo,

                id_perfilUsuario = funcionarioForm.perfilUsuario.data,

                id_endereco = Endereco.id,

                telefone = funcionarioForm.telefone.data,
                celular = funcionarioForm.celular.data,
                email = funcionarioForm.email.data,
                frete = funcionarioForm.frete.data,
                observacoes = funcionarioForm.observacoes.data,

                id_view = view.id,
                id_inicioview = inicio.id
            )
            db.session.add(funcionario)
            db.session.commit()
            flash('Usuário Registrado com sucesso! Senha pré-definida é somente os numeros do cpf. Após o login poderá alterar a senha!', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar usuário', 'danger')

        return redirect(url_for('usuarios.clientes')) 

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/clientes/cadastrar.html', 
                            funcionarioForm = funcionarioForm,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/clientes/editar/<id>', methods=['GET', 'POST'])
@login_required
def editarCliente(id):
    controle = 0
    funcionarioForm = FuncionarioForm()
    funcionario = Cliente.query.filter_by(id=id).first_or_404()

    perfil = perfilUsuario.query.all()
    funcionarioForm.perfilUsuario.choices = [(funcionario.perfilUsuario.id, funcionario.perfilUsuario.nome)]

    for perf in perfil: 
        if perf.id == 6:       
            funcionarioForm.perfilUsuario.choices += [(perf.id, perf.nome)]

    funcionarioForm.UF.choices = [(funcionario.endereco.uf, funcionario.endereco.uf)]
    for valor in ufbr.list_uf:
        funcionarioForm.UF.choices += [(valor, valor)]
    funcionarioForm.municipio.choices = [(funcionario.endereco.municipio, funcionario.endereco.municipio)]
    for valor in ufbr.list_cidades(funcionario.endereco.uf):
        funcionarioForm.municipio.choices += [(valor, valor)]

    funcionarioForm.pais.choices = [(funcionario.endereco.pais, funcionario.endereco.pais)]

    funcionarioForm.observacoes.data = funcionario.observacoes
    
    if funcionarioForm.cancelar.data == True and request.method == 'POST':
        return redirect(url_for('usuarios.clientes'))
    
    if funcionarioForm.salvar.data == True and request.method == 'POST':

        myFunc = Usuario.query.filter_by(id=id).first_or_404()
       
        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = myFunc.imagem

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
            arquivo = myFunc.imagem

        if myFunc:
            myFunc.nome = funcionarioForm.nome.data
            myFunc.CPF = funcionarioForm.cpf.data            
            myFunc.dataNascimento = funcionarioForm.dataNascimento.data            
            myFunc.imagem = arquivo
            myFunc.frete = funcionarioForm.frete.data
            myFunc.telefone = funcionarioForm.telefone.data
            myFunc.celular = funcionarioForm.celular.data 
            myFunc.email = funcionarioForm.email.data

            myFunc.endereco.uf = funcionarioForm.UF.data
            myFunc.endereco.municipio = funcionarioForm.municipio.data
            myFunc.endereco.pais = funcionarioForm.pais.data
            myFunc.endereco.cep = funcionarioForm.CEP.data
            myFunc.endereco.endereco = funcionarioForm.endereco.data
            myFunc.endereco.numero = funcionarioForm.numero.data
            myFunc.endereco.complemento = funcionarioForm.complemento.data
            myFunc.endereco.bairro = funcionarioForm.bairro.data
            try:
                db.session.commit()
                flash('Registro alterado com sucesso', 'success')
                return redirect(url_for('usuarios.clientes'))
            except:
                db.session.rollback()
                flash('Registro falhou em alterar', 'danger')                

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('usuarios/clientes/editar.html', 
                            funcionario=funcionario, 
                            funcionarioForm = funcionarioForm, 
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/clientes/visualizar/<id>', methods=['GET', 'POST'])
@login_required
def visualizarCliente(id):
    funcionario = Cliente.query.filter_by(id=id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/clientes/visualizar.html', 
                            meuPerfil=funcionario,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/clientes/excluir/<id>', methods=['GET', 'POST'])
@login_required
def excluirCliente(id):
    confirma = excluirForm()
    funcionario = Cliente.query.filter_by(id=id).first_or_404()

    if confirma.s.data == True: 
        if current_user.id == funcionario.id:
            flash('Não é possivel excluir usuario atualmente em uso, entre com outro usuário para excluir este.', 'danger')
            return redirect(url_for('usuarios.index'))       
        try:
            db.session.delete(funcionario)
            db.session.commit()
            flash('Cliente excluido com sucesso', 'success')
            return redirect(url_for('usuarios.index'))
        except:
            db.session.rollback()
            flash('Cliente não foi excluido', 'danger')
            return redirect(url_for('usuarios.index'))
            
    if confirma.n.data == True: 
        flash('Cliente não foi excluido!', 'warning')
        return redirect(url_for('usuarios.index'))
    
    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/excluirFuncionario.html',  
                            meuPerfil=funcionario, 
                            confirma=confirma,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/usuarios', methods=['GET', 'POST'])
@login_required
def index():
    funcionarios = Usuario.query.all()
    view = View.query.filter_by(id = current_user.id_view).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('usuarios/tabela.html', 
                            funcionarios = funcionarios, 
                            view = view,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/usuarios/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrar():
    controle = 0
    funcionarioForm = FuncionarioForm()

    perfil = perfilUsuario.query.all()
    for perf in perfil: 
        if current_user.perfilUsuario.id <= perf.id:       
            funcionarioForm.perfilUsuario.choices += [(perf.id, perf.nome)]
            

    funcionarioForm.UF.choices = [('RS', 'RS')]
    for valor in ufbr.list_uf:
        funcionarioForm.UF.choices += [(valor, valor)]
    funcionarioForm.municipio.choices = [('Selecione uma opção', 'Selecione uma opção')]
    for valor in ufbr.list_cidades('RS'):
        funcionarioForm.municipio.choices += [(valor, valor)]

    if funcionarioForm.cancelar.data == True and request.method == 'POST':
        return redirect(url_for('usuarios.index'))

    if funcionarioForm.salvar.data == True and request.method == 'POST':
        # Seta a senha padrão o cpf sem caracteres especiais
        novaSenha = funcionarioForm.cpf.data.replace('.','').replace('-','')
        try:
            Endereco = endereco(
                uf = funcionarioForm.UF.data,
                municipio = funcionarioForm.municipio.data,
                pais = funcionarioForm.pais.data,
                cep = funcionarioForm.CEP.data,
                endereco = funcionarioForm.endereco.data,
                numero = funcionarioForm.numero.data,
                complemento = funcionarioForm.complemento.data,
                bairro = funcionarioForm.bairro.data
            )
            db.session.add(Endereco)            
            db.session.commit()
            # flash('Endereço Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar endereço', 'danger')

        # ADICIONANDO AS VIEWS DO FUNCIONARIO 
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
            # flash('View Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar View', 'danger')
        try:
            inicio = InicioView(
                cliente = True,
                funcionario = True,
                pedido = True,
                estoque = True,
                graficoPedidos = True
            )            
            db.session.add(inicio)            
            db.session.commit()
            # flash('View Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar View', 'danger')
        # Finalizando a criação das views

        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = 'default-user.jpg'

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
            arquivo = 'default-user.jpg'
        try:            
            funcionario = Usuario(
                nome = funcionarioForm.nome.data,
                CPF = funcionarioForm.cpf.data,
                dataNascimento = funcionarioForm.dataNascimento.data,
                password = novaSenha,
                imagem =  arquivo,

                id_perfilUsuario = funcionarioForm.perfilUsuario.data,

                id_endereco = Endereco.id,

                telefone = funcionarioForm.telefone.data,
                celular = funcionarioForm.celular.data,
                email = funcionarioForm.email.data,
                frete = funcionarioForm.frete.data,
                observacoes = funcionarioForm.observacoes.data,

                id_view = view.id,
                id_inicioview = inicio.id
            )
            db.session.add(funcionario)
            db.session.commit()
            flash('Usuário Registrado com sucesso! Senha pré-definida é somente os numeros do cpf. Após o login poderá alterar a senha!', 'success')
        except:
            db.session.rollback()
            flash('Falha ao adicionar usuário', 'danger')

        return redirect(url_for('usuarios.index')) 

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/cadastroFuncionario.html', 
                            funcionarioForm = funcionarioForm,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/usuario/visualizar/<id>', methods=['GET', 'POST'])
@login_required
def visualizar(id):
    funcionario = Usuario.query.filter_by(id=id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/visualizarFuncionario.html', 
                            meuPerfil=funcionario,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/usuario/editar/<id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    controle = 0
    funcionarioForm = FuncionarioForm()
    funcionario = Usuario.query.filter_by(id=id).first_or_404()

    perfil = perfilUsuario.query.all()
    funcionarioForm.perfilUsuario.choices = [(funcionario.perfilUsuario.id, funcionario.perfilUsuario.nome)]

    for perf in perfil: 
        if current_user.perfilUsuario.id <= perf.id:       
            funcionarioForm.perfilUsuario.choices += [(perf.id, perf.nome)]

    funcionarioForm.UF.choices = [(funcionario.endereco.uf, funcionario.endereco.uf)]
    for valor in ufbr.list_uf:
        funcionarioForm.UF.choices += [(valor, valor)]
    funcionarioForm.municipio.choices = [(funcionario.endereco.municipio, funcionario.endereco.municipio)]
    for valor in ufbr.list_cidades(funcionario.endereco.uf):
        funcionarioForm.municipio.choices += [(valor, valor)]

    funcionarioForm.pais.choices = [(funcionario.endereco.pais, funcionario.endereco.pais)]

    funcionarioForm.observacoes.data = funcionario.observacoes
    
    if funcionarioForm.cancelar.data == True and request.method == 'POST':
        return redirect(url_for('usuarios.index'))
    
    if funcionarioForm.salvar.data == True and request.method == 'POST':

        myFunc = Usuario.query.filter_by(id=id).first_or_404()
       
        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = myFunc.imagem

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
            arquivo = myFunc.imagem

        if myFunc:
            myFunc.nome = funcionarioForm.nome.data
            myFunc.CPF = funcionarioForm.cpf.data            
            myFunc.dataNascimento = funcionarioForm.dataNascimento.data            
            myFunc.imagem = arquivo
            myFunc.frete = funcionarioForm.frete.data
            myFunc.telefone = funcionarioForm.telefone.data
            myFunc.celular = funcionarioForm.celular.data 
            myFunc.email = funcionarioForm.email.data

            myFunc.endereco.uf = funcionarioForm.UF.data
            myFunc.endereco.municipio = funcionarioForm.municipio.data
            myFunc.endereco.pais = funcionarioForm.pais.data
            myFunc.endereco.cep = funcionarioForm.CEP.data
            myFunc.endereco.endereco = funcionarioForm.endereco.data
            myFunc.endereco.numero = funcionarioForm.numero.data
            myFunc.endereco.complemento = funcionarioForm.complemento.data
            myFunc.endereco.bairro = funcionarioForm.bairro.data
            try:
                db.session.commit()
                flash('Registro alterado com sucesso', 'success')
                return redirect(url_for('usuarios.index'))
            except:
                db.session.rollback()
                flash('Registro falhou em alterar', 'danger')                

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('usuarios/editarFuncionario.html', 
                            funcionario=funcionario, 
                            funcionarioForm = funcionarioForm, 
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@usuarios.route('/usuario/excluir/<id>', methods=['GET', 'POST'])
@login_required
def excluir(id):
    confirma = excluirForm()
    funcionario = Usuario.query.filter_by(id=id).first_or_404()

    if confirma.s.data == True: 
        if current_user.id == funcionario.id:
            flash('Não é possivel excluir usuario atualmente em uso, entre com outro usuário para excluir este.', 'danger')
            return redirect(url_for('usuarios.index'))       
        try:
            db.session.delete(funcionario)
            db.session.commit()
            flash('Funcionario excluido com sucesso', 'success')
            return redirect(url_for('usuarios.index'))
        except:
            db.session.rollback()
            flash('Funcionário não foi excluido', 'danger')
            return redirect(url_for('usuarios.index'))
            
    if confirma.n.data == True: 
        flash('Funcionário não foi excluido!', 'warning')
        return redirect(url_for('usuarios.index'))
    
    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/excluirFuncionario.html',  
                            meuPerfil=funcionario, 
                            confirma=confirma,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
    
@usuarios.route('/usuario/editarViews', methods=['GET', 'POST'])
@login_required
def editarView():
    minhaView = Usuario.query.filter_by(id=current_user.id).first_or_404()
    viewform = viewForm()

    if viewform.cancelar.data == True:
        flash('Nada foi alterado', 'warning')
        return redirect(url_for('usuarios.index'))
        
    if viewform.salvar.data == True:
        if minhaView:
            minhaView.view.nomeView = viewform.viewFormfuncionario.data
            minhaView.view.CPFView = viewform.viewFormCPF.data

            minhaView.view.UFView = viewform.viewFormUF.data
            minhaView.view.municipioView = viewform.viewFormmunicipio.data
            minhaView.view.paisView = viewform.viewFormpais.data
            minhaView.view.CEPView = viewform.viewFormCEP.data
            minhaView.view.enderecoView = viewform.viewFormendereco.data
            minhaView.view.numeroView = viewform.viewFormnumero.data
            minhaView.view.complementoView = viewform.viewFormcomplemento.data
            minhaView.view.bairroView = viewform.viewFormbairro.data

            minhaView.view.telefoneView = viewform.viewFormtelefone.data
            minhaView.view.celularView = viewform.viewFormcelular.data
            minhaView.view.emailView = viewform.viewFormemail.data
            
            try:
                db.session.commit()
                flash('Registro alterado com sucesso', 'success')
                return redirect(url_for('usuario.index'))
            except:
                db.session.rollback()
                flash('Falha em alterar o registro', 'danger')

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/editarViews.html', 
                            meuPerfil = minhaView, 
                            viewForm = viewform, 
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days)
    
@usuarios.route('/usuario/editarSenha/<id>', methods=['GET', 'POST'])
@login_required
def editarSenha(id):
    
    funcionarioForm = FuncionarioForm()

    meuperfil = Usuario.query.filter_by(id=id).first_or_404()
    
    myFunc = Usuario.query.filter_by(id=id).first_or_404()

    if request.method == 'POST' and funcionarioForm.cancelar.data == True:
        db.session.rollback()
        flash('Operação cancelada', 'warning')
        return redirect(url_for('usuarios.index'))

    if request.method == 'POST' and funcionarioForm.salvar.data == True:
        if funcionarioForm.senha.data == '':
            flash('Campo senha vazio não é permitido', 'warning')
            db.session.rollback()
            return redirect(url_for('usuario.editarSenha', id=myFunc.id))
            
        if myFunc:
            if funcionarioForm.senha.data == funcionarioForm.confirmarSenha.data:
                myFunc.password = funcionarioForm.senha.data
                try:
                    db.session.commit()
                    flash('Senha alterada com sucesso', 'success')
                    return redirect(url_for('usuario.index'))
                except:
                    db.session.rollback()
                    flash('Não foi possivel alterar a senha!', 'danger')
            else:
                flash('Senhas não conferem', 'warning')
                db.session.rollback()
                return redirect(url_for('usuario.editarSenha', id=myFunc.id))

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('usuarios/editarSenha.html', 
                            FuncionarioForm = funcionarioForm,
                            meuPerfil = meuperfil,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )