import os
from random import randint
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user

from pyUFbr.baseuf import ufbr

from datetime import datetime

from app import db
from app.loja.forms import FotoUploadForm, MarcaUploadForm, AnuncioForm
from . import loja
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, Banner, Categoria, perfilUsuario

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

import os
if os.name == 'nt':
    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
else:
    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@loja.route('/', methods=['GET', 'POST'])
def index():    
    return redirect(url_for('auth.login'))

    cfg = config.query.filter_by(id=1).first()
    if cfg is None:
        return redirect(url_for('install.index'))
        
    ban = Banner.query.all()
    produtos = Estoque.query.all()

    idMax = 0
    for produto in produtos:
        if idMax < produto.id:
            idMax = produto.id
    

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/index.html', config = configuracao, banner = ban, produtos = produtos, idMax = idMax)

@loja.route('/carrinho', methods=['GET', 'POST'])
def carrino():
    
    return redirect(url_for('auth.login'))

    produtos = Estoque.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/carrinho.html', config = configuracao, produtos = produtos)

@loja.route('/produtos', methods=['GET', 'POST'])
def produtos():

    return redirect(url_for('auth.login'))

    produtos = Estoque.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/produtos.html', config = configuracao, produtos = produtos)

@loja.route('/sistemaGestao', methods=['GET', 'POST'])
def sistemaGestao():

    return redirect(url_for('auth.login'))

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/sistemaGestao.html', config = configuracao)

@loja.route('/suporteLocal', methods=['GET', 'POST'])
def suporteLocal():

    return redirect(url_for('auth.login'))

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/suporteLocal.html', config = configuracao)

@loja.route('/contato', methods=['GET', 'POST'])
def contato():

    return redirect(url_for('auth.login'))

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/contato.html', config = configuracao)



# Administrativo
@loja.route('/loja', methods=['GET', 'POST'])
@login_required
def lojaVirtual():

    return redirect(url_for('auth.login'))

    ban = Banner.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/admin/index.html', config = configuracao, banner = ban)

@loja.route('/banner', methods=['GET', 'POST'])
@login_required
def indexBanner():

    return redirect(url_for('auth.login'))

    ban = Banner.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/admin/banner/index.html', config = configuracao, banner = ban)

@loja.route('/banner/adicionarBanner', methods=['GET', 'POST'])
@login_required
def adicionarBanner():

    return redirect(url_for('auth.login'))

    form = FotoUploadForm()
    controle = 0

    if request.method == 'POST' and form.descartar.data == True:
        return redirect(url_for('loja.indexBanner'))

    if request.method == 'POST' and form.enviar.data == True:

        # Checando qual o maior status no momento
        banner = Banner.query.all()
        maxStatus = 0
        for st in banner:
            if maxStatus <= st.ordem:
                maxStatus = st.ordem
        maxStatus = maxStatus + 1

        if 'banner' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:
            file = request.files['banner']
            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    controle = 1

        if controle == 1:
            db.session.rollback()
            flash('Falha ao adicionar banner', 'danger')
            return redirect(url_for('loja.indexBanner'))

        if file and allowed_file(file.filename):
            import os
            if os.name == 'nt':
                UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\banners\\'
            else:
                UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/banners/'

            stri = datetime.utcnow().timestamp()
            newfilename = str(stri)+"-"+file.filename

            file.save(os.path.join(UPLOAD_FOLDER, newfilename))
            arquivo = newfilename

        try:
            banner = Banner(
                ordem = maxStatus,
                nome = arquivo
            )
            db.session.add(banner)
            db.session.commit()
            flash('Banner cadastrado com sucesso', 'success')
            return redirect(url_for('loja.indexBanner'))
        except:
            db.session.rollback()
            flash('Falha ao adicionar banner', 'danger')
            return redirect(url_for('loja.indexBanner'))


    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/admin/banner/adicionarBanner.html', config = configuracao, form = form)

@loja.route('/banner/editarBanner/<id>', methods=['GET', 'POST'])
@login_required
def editarBanner(id):

    return redirect(url_for('auth.login'))

    form = FotoUploadForm()
    controle = 0
    if request.method == 'POST' and form.descartar.data == True:
        return redirect(url_for('loja.indexBanner'))

    if request.method == 'POST' and form.enviar.data == True:
        oldBanner = Banner.query.filter_by(id=id).first_or_404()
        if oldBanner:
            if 'banner' not in request.files:
                flash('Arquivo nao anexado','info')
                controle = 1
            if controle == 0:
                file = request.files['banner']
                if file.filename == '':
                        flash('Nenhum arquivo selecionado','info')
                        arquivo = oldBanner.nome
                if file and allowed_file(file.filename):
                    import os
                    if os.name == 'nt':
                        UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\banners\\'
                    else:
                        UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/banners/'
                    stri = datetime.utcnow().timestamp()
                    newfilename = str(stri)+"-"+file.filename
                    file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                    arquivo = newfilename
                    caminhoAntigo = UPLOAD_FOLDER+oldBanner.nome
                    os.remove(caminhoAntigo)
            else:
                arquivo = oldBanner.nome
        try:
            oldBanner.nome = arquivo
            db.session.commit()
            flash('Banner alterado com sucesso', 'success')
            return redirect(url_for('loja.indexBanner'))
        except:
            db.session.rollback()
            flash('Falha ao alterar banner', 'danger')
            return redirect(url_for('loja.indexBanner'))

    ban = Banner.query.filter_by(id = id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('loja/admin/banner/editarBanner.html', config = configuracao, form = form, banner = ban)

@loja.route('/banner/excluirBanner/<id>', methods=['GET', 'POST'])
@login_required
def excluirBanner(id):

    return redirect(url_for('auth.login'))

    banner = Banner.query.filter_by(id=id).first_or_404()
    import os
    if os.name == 'nt':
        UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\banners\\'
    else:
        UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/banners/'
    caminhoAntigo = UPLOAD_FOLDER+banner.nome
    os.remove(caminhoAntigo)
    try:
        db.session.delete(banner)
        db.session.commit()
        return jsonify({'url' : url_for('loja.indexBanner'),
                        'mensagem' : 'Banner excluido com sucesso',
                        'cor' : 'success'
                        })
    except:
        db.session.rollback()
        return jsonify({'url' : url_for('loja.indexBanner'),
                        'mensagem' : 'Banner não foi excluido',
                        'cor' : 'danger'
                        })

    return redirect(url_for('loja.indexBanner'))
