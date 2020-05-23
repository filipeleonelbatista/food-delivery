import os
from random import randint

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from app import db
from app.estoque.forms import EstoqueForm, editarViewForm, excluirForm, categoriaForm
from . import estoque
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, Categoria, perfilUsuario
from datetime import datetime

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

import os
if os.name == 'nt':
    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\products\\'
else:
    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/products/'


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@estoque.route('/estoque')
@login_required
def index():
    configuracao = config.query.filter_by(id=1).first_or_404()

    estoque = Estoque.query.all()
    return render_template('estoque/tabela.html',
                            config = configuracao,
                            produtos = estoque,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
@estoque.route('/estoque/cadastroCategoria', methods=['GET', 'POST'])
@login_required
def cadastroCategoria():
    cat = Categoria.query.all()
    form = categoriaForm()

    if form.cancelar.data == True and request.method == 'POST':
        flash('categoria nao cadastrada','warning')
        return redirect(url_for('estoque.index'))

    if form.salvar.data == True and request.method == 'POST':
      
        try:
            categoria = Categoria(
                categoria = form.categoria.data
            )
            db.session.add(categoria)            
            db.session.commit()
            flash('Categoria cadastrada com sucesso', 'success')
            return redirect(url_for('estoque.index'))
        except:
            db.session.rollback()
            flash('Falha ao adicionar categoria', 'danger')                
            return redirect(url_for('estoque.index'))
        

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('estoque/cadastroCategoria.html', 
                            form = form,
                            config = configuracao,
                            categorias = cat,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@estoque.route('/estoque/excluirCategoria', methods=['GET', 'POST'])
@login_required
def excluirCategoria():
    cat = Categoria.query.all()

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('estoque/excluirCategoria.html', 
                            categorias = cat,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@estoque.route('/estoque/excluirCat/<id>', methods=['GET', 'POST'])
@login_required
def excluirCat(id):
    cat = Categoria.query.filter_by(id=id).first_or_404()
    produtos = Estoque.query.filter_by(id_categoria=cat.id).all()
    if len(produtos)==0:
        try:
            db.session.delete(cat)
            db.session.commit()
            flash('Categoria excluida com sucesso', 'success')
            return redirect(url_for('estoque.index'))
        except:
            db.session.rollback()
            flash('Categoria não pode ser excluida', 'danger')
            return redirect(url_for('estoque.excluirCategoria'))
    else:
        if len(produtos) == 1:
            flash('Categoria {0} Não foi excluida pois tem {1} produto dentro desta categoria.'.format(cat.categoria,len(produtos)), 'warning')
        else:
            flash('Categoria {0} Não foi excluida pois tem {1} produtos dentro desta categoria.'.format(cat.categoria,len(produtos)), 'warning')
        return redirect(url_for('estoque.excluirCategoria'))

    return id

@estoque.route('/estoque/cadastroProduto', methods=['GET', 'POST'])
@login_required
def cadastroProduto():
    estoqueForm = EstoqueForm()
    controle = 0

    categorias = Categoria.query.all()

    for categoria in categorias:
        estoqueForm.categoria.choices += [(categoria.id, categoria.categoria)]

    if estoqueForm.cancelar.data == True and request.method == 'POST':
        flash('Produto nao foi cadastrado','warning')
        return redirect(url_for('estoque.index'))

    if estoqueForm.salvar.data == True and request.method == 'POST':
        if estoqueForm.precoVenda.data == '' or estoqueForm.precoVenda.data == ' ':
            estoqueForm.precoVenda.data = '0,00'   
        if estoqueForm.descricaoProduto.data == '' or estoqueForm.descricaoProduto.data == ' ':
            estoqueForm.descricaoProduto.data = 'Sem descrição' 
        if estoqueForm.nomeProduto.data == '' or estoqueForm.nomeProduto.data == ' ':
            estoqueForm.nomeProduto.data = 'Sem nome'  
        
        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = 'default-produto.png'

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/products/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                arquivo = newfilename
        else:
            arquivo = 'default-produto.png'
        
        try:
            produto = Estoque(
                nomeProduto = estoqueForm.nomeProduto.data,
                descricaoProduto = estoqueForm.descricaoProduto.data,
                precoVenda = estoqueForm.precoVenda.data,
                imagem = arquivo,
                id_categoria = estoqueForm.categoria.data
            )
            db.session.add(produto)            
            db.session.commit()
            flash('Produto cadastrado com sucesso', 'success')
            return redirect(url_for('estoque.index'))
        except:
            db.session.rollback()
            flash('Falha ao adicionar cliente', 'danger')                
            return redirect(url_for('estoque.index'))
        else:
            flash("Codigo de Barras ja existe, Favor Gerar novo codigo!", "danger")

    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('estoque/cadastroProduto.html', 
                            estoqueForm = estoqueForm,
                            config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@estoque.route('/estoque/visualizarProduto/<id>', methods=['GET', 'POST'])
@login_required
def visualizarProduto(id):
    cEstoque = Estoque.query.filter_by(id = id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('estoque/visualizarProduto.html', 
                            config = configuracao,
                            cView = cEstoque,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
                            
@estoque.route('/estoque/editarProduto/<id>', methods=['GET', 'POST'])
@login_required
def editarProduto(id):
    controle = 0
    eForm = EstoqueForm()
    cEstoque = Estoque.query.filter_by(id = id).first_or_404()
    allCat = Categoria.query.all()
    
    eForm.categoria.choices = []
    eForm.categoria.choices += [(cEstoque.categoria.id,cEstoque.categoria.categoria)]
    for cat in allCat:
        eForm.categoria.choices += [(cat.id,cat.categoria)]    

    if eForm.cancelar.data == True and request.method == 'POST':
        flash("Nada foi alterado!","warning")
        return redirect(url_for('estoque.index'))

    if eForm.salvar.data == True and request.method == 'POST':

        if eForm.precoVenda.data == '' or eForm.precoVenda.data == ' ':
            eForm.precoVenda.data = '0,00'   
        if eForm.descricaoProduto.data == '' or eForm.descricaoProduto.data == ' ':
            eForm.descricaoProduto.data = 'Sem descrição' 
        if eForm.nomeProduto.data == '' or eForm.nomeProduto.data == ' ':
            eForm.nomeProduto.data = 'Sem nome' 

        # Inserir o upload aqui
        if 'imagem' not in request.files:
            flash('Arquivo nao anexado','info')
            controle = 1
            arquivo = cEstoque.imagem

        if controle == 0:            
            file = request.files['imagem']

            if file.filename == '':
                    flash('Nenhum arquivo selecionado','info')
                    arquivo = cEstoque.imagem

            if file and allowed_file(file.filename):
                import os
                if os.name == 'nt':
                    UPLOAD_FOLDER = os.getcwd()+'\\app\\static\\images\\'
                else:
                    UPLOAD_FOLDER = os.getcwd()+'/projeto_crm/app/static/images/products/'

                stri = datetime.utcnow().timestamp()
                newfilename = str(stri)+"-"+file.filename

                file.save(os.path.join(UPLOAD_FOLDER, newfilename))
                arquivo = newfilename
        else:
            arquivo = cEstoque.imagem
        
        if cEstoque:
            cEstoque.nomeProduto = eForm.nomeProduto.data
            cEstoque.descricaoProduto = eForm.descricaoProduto.data
            cEstoque.precoVenda = eForm.precoVenda.data
            cEstoque.id_categoria = eForm.categoria.data
            cEstoque.imagem = arquivo
            try:
                db.session.commit()
                flash('Produto alterado com sucesso', 'success')
                return redirect(url_for('estoque.index'))
            except:
                db.session.rollback()
                flash('Falha ao alterar produto', 'danger')

    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('estoque/editarProduto.html', 
                            config = configuracao,
                            cView = cEstoque,
                            estoqueForm = eForm,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@estoque.route('/estoque/excluirProduto/<id>', methods=['GET', 'POST'])
@login_required
def excluirProduto(id):
    eForm = EstoqueForm()
    confirmaForm = excluirForm()
    cEstoque = Estoque.query.filter_by(id = id).first_or_404()

    if confirmaForm.n.data == True and request.method == 'POST':
        flash("Nada foi alterado!","warning")
        return redirect(url_for('estoque.index'))

    if confirmaForm.s.data == True and request.method == 'POST':
        verificaProduto = Item.query.filter_by(id = cEstoque.id)
        try:
            db.session.delete(cEstoque)
            db.session.commit()
            flash('Produto excluido com sucesso', 'success')
            return redirect(url_for('estoque.index'))
        except:
            db.session.rollback()
            flash('Produto não excluido', 'danger')
            return redirect(url_for('estoque.index'))


    configuracao = config.query.filter_by(id=1).first_or_404()    
    return render_template('estoque/excluirProduto.html', 
                            config = configuracao,
                            cView = cEstoque,
                            estoqueForm = eForm,
                            confirma = confirmaForm,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )