import os
from random import randint
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user

from datetime import datetime

from app import db
from app.configuracao.forms import empresaForm, cargoForm, excluirForm, statusForm
from . import configuracao
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, Categoria, perfilUsuario, status

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

import os
if os.name == 'nt':
    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
else:
    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@configuracao.route('/configuracao', methods=['GET', 'POST'])
@login_required
def index():
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/index.html', 
                            config = configuracao,  
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/editarInfoComercial', methods=['GET', 'POST'])
@login_required
def editarInfoComercial():    
    EmpresaForm = empresaForm()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/editarInfoComercial.html', 
                            config = configuracao,                          
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/iconeLogo', methods=['GET', 'POST'])
@login_required
def iconeLogo():
    EmpresaForm = empresaForm()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/iconeLogo.html', 
                            config = configuracao,                         
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/impressao', methods=['GET', 'POST'])
@login_required
def impressao():
    EmpresaForm = empresaForm()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/impressao.html', 
                            config = configuracao,                         
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/editarDescricao', methods=['GET', 'POST'])
@login_required
def editarDescricao():
    EmpresaForm = empresaForm()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/editarDescricao.html', 
                            config = configuracao,                         
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/editarStatusPadrao', methods=['GET', 'POST'])
@login_required
def editarStatusPadrao():
    EmpresaForm = empresaForm()
    stat = status.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('configuracao/editarStatusPadrao.html', 
                            config = configuracao,   
                            status = stat,                      
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days)

@configuracao.route('/configuracao/empresa', methods=['GET', 'POST'])
@login_required
def empresa():
    EmpresaForm = empresaForm()
    newConfig = config.query.filter_by(id=1).first_or_404()
    controle = 0
    controle1 = 0

    if EmpresaForm.cancelar.data == True and request.method == 'POST':        
       db.session.rollback()
       flash("Configurações nao foram alteradas","warning")
       return redirect(url_for('configuracao.index')) 

    if request.method == 'POST' and EmpresaForm.salvar.data == True:
        novoFotoEmpresa = ''
        if 'icon' not in request.files:
            flash('Arquivo nao anexado','warning')
            controle = 1

        if controle == 0:
            file = request.files['icon']
            if file.filename == '':
                    flash('Nenhum arquivo selecionado', "primary")
                    novoIcone = newConfig.icon

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                novoIcone = newfilename
        else:
            novoIcone = newConfig.icon

        if 'logo' not in request.files:
            flash('Arquivo nao anexado','warning')
            controle1 = 1

        if controle1 == 0:
            file = request.files['logo']
            if file.filename == '':
                    flash('Nenhum arquivo selecionado', "primary")
                    novoLogo = newConfig.logo

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                novoLogo = newfilename 
        else:
            novoLogo = newConfig.logo

        if current_user.id == 1:
            if newConfig:
                newConfig.razaoSocial = EmpresaForm.razaoSocial.data
                newConfig.nomeFantasia = EmpresaForm.nomeFantasia.data
                newConfig.CNPJ = EmpresaForm.CNPJ.data
                newConfig.imprimir = EmpresaForm.imprimir.data
                newConfig.tipoImpressao = EmpresaForm.imprimirTermica.data
                newConfig.ativa = EmpresaForm.ativo.data
                newConfig.whatsapp = EmpresaForm.whatsapp.data
                newConfig.facebook = EmpresaForm.facebook.data
                newConfig.facebookPgId = EmpresaForm.facebookPgId.data
                newConfig.twitter = EmpresaForm.twitter.data
                newConfig.instagram = EmpresaForm.instagram.data
                newConfig.youtube = EmpresaForm.youtube.data
                newConfig.linkedin = EmpresaForm.linkedin.data
                newConfig.telefone = EmpresaForm.telefone.data
                newConfig.descricao = EmpresaForm.descricao.data
                newConfig.sobre = EmpresaForm.sobre.data
                newConfig.email = EmpresaForm.email.data
                newConfig.icon = novoIcone
                newConfig.logo = novoLogo
                newConfig.endereco.UF = EmpresaForm.UF.data
                newConfig.endereco.municipio = EmpresaForm.municipio.data
                newConfig.endereco.pais = EmpresaForm.pais.data
                newConfig.endereco.CEP = EmpresaForm.CEP.data
                newConfig.endereco.endereco = EmpresaForm.endereco.data
                newConfig.endereco.numero = EmpresaForm.numero.data
                newConfig.endereco.complemento = EmpresaForm.complemento.data
                newConfig.endereco.bairro = EmpresaForm.bairro.data

                newConfig.update = EmpresaForm.update.data
                newConfig.sobreUpdate = EmpresaForm.sobreUpdate.data
                try:
                    db.session.commit()
                    flash('Informações da empresa atualizadas', 'success')
                    return redirect(url_for('configuracao.index'))
                except:
                    db.session.rollback()
                    flash('Não foi possivel atualizar as informações da empresa.', 'danger')

        else:
            if newConfig:
                newConfig.razaoSocial = EmpresaForm.razaoSocial.data
                newConfig.nomeFantasia = EmpresaForm.nomeFantasia.data
                newConfig.CNPJ = EmpresaForm.CNPJ.data
                newConfig.imprimir = EmpresaForm.imprimir.data
                newConfig.tipoImpressao = EmpresaForm.imprimirTermica.data
                newConfig.whatsapp = EmpresaForm.whatsapp.data
                newConfig.facebook = EmpresaForm.facebook.data
                newConfig.facebookPgId = EmpresaForm.facebookPgId.data
                newConfig.twitter = EmpresaForm.twitter.data
                newConfig.instagram = EmpresaForm.instagram.data
                newConfig.youtube = EmpresaForm.youtube.data
                newConfig.linkedin = EmpresaForm.linkedin.data
                newConfig.telefone = EmpresaForm.telefone.data
                newConfig.descricao = EmpresaForm.descricao.data
                newConfig.sobre = EmpresaForm.sobre.data
                newConfig.email = EmpresaForm.email.data
                newConfig.icon = novoIcone
                newConfig.logo = novoLogo
                newConfig.endereco.UF = EmpresaForm.UF.data
                newConfig.endereco.municipio = EmpresaForm.municipio.data
                newConfig.endereco.pais = EmpresaForm.pais.data
                newConfig.endereco.CEP = EmpresaForm.CEP.data
                newConfig.endereco.endereco = EmpresaForm.endereco.data
                newConfig.endereco.numero = EmpresaForm.numero.data
                newConfig.endereco.complemento = EmpresaForm.complemento.data
                newConfig.endereco.bairro = EmpresaForm.bairro.data

                newConfig.ativa = newConfig.ativa
                newConfig.update = newConfig.update
                newConfig.sobreUpdate = newConfig.sobreUpdate
                try:
                    db.session.commit()
                    flash('Informações da empresa atualizadas', 'success')
                    return redirect(url_for('configuracao.index'))
                except:
                    db.session.rollback()
                    flash('Não foi possivel atualizar as informações da empresa.', 'danger')
            
        
    configuracao = config.query.filter_by(id=1).first_or_404()
    EmpresaForm.descricao.data = configuracao.descricao
    EmpresaForm.sobre.data = configuracao.sobre    
    EmpresaForm.sobreUpdate.data = configuracao.sobreUpdate
    EmpresaForm.municipio.choices = [(configuracao.endereco.municipio,configuracao.endereco.municipio)]
    EmpresaForm.UF.choices = [(configuracao.endereco.uf,configuracao.endereco.uf)]
    EmpresaForm.pais.choices = [(configuracao.endereco.pais,configuracao.endereco.pais)]
    return render_template('configuracao/editarEmpresa.html', 
                            config = configuracao,
                            form = EmpresaForm,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
