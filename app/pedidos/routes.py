import os
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

import json
from flask import jsonify

from datetime import datetime

from app import db
from app.pedidos.forms import pedidoForm, itensForm, confirmForm
from . import pedidos
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Cliente, Item, Pedido, Categoria, perfilUsuario, status

@pedidos.route('/pedidos/proxStatusEntregas/<id>', methods=['GET', 'POST'])
@login_required
def proxStatusEntregas(id):
    pedido = Pedido.query.filter_by(id=id).first()
    statusAtual = pedido.status.ordem + 1
    novoStatus = status.query.filter_by(ordem=statusAtual).first()
    if novoStatus is None:
        flash("Não existem novos status", "warning")
        return redirect(url_for('pedidos.entregas'))
    else:
        try:
            pedido.id_status = novoStatus.id
            db.session.commit()
            flash("Status atualizado com suscesso", "success")
            return redirect(url_for('pedidos.entregas'))
        except:
            db.session.rollback()
            flash("Erro ao atualizar o status")
            return redirect(url_for('pedidos.entregas'))

@pedidos.route('/pedidos/proxStatusCozinha/<id>', methods=['GET', 'POST'])
@login_required
def proxStatusCozinha(id):
    pedido = Pedido.query.filter_by(id=id).first()
    statusAtual = pedido.status.ordem + 1
    novoStatus = status.query.filter_by(ordem=statusAtual).first()
    if novoStatus is None:
        flash("Não existem novos status", "warning")
        return redirect(url_for('pedidos.cozinha'))
    else:
        try:
            pedido.id_status = novoStatus.id
            db.session.commit()
            flash("Status atualizado com suscesso", "success")
            return redirect(url_for('pedidos.cozinha'))
        except:
            db.session.rollback()
            flash("Erro ao atualizar o status")
            return redirect(url_for('pedidos.cozinha'))

@pedidos.route('/pedidos/proximoStatus/<id>', methods=['GET', 'POST'])
@login_required
def proxStatus(id):
    pedido = Pedido.query.filter_by(id=id).first()
    statusAtual = pedido.status.ordem + 1
    novoStatus = status.query.filter_by(ordem=statusAtual).first()
    if novoStatus is None:
        flash("Não existem novos status", "warning")
        return redirect(url_for('pedidos.index'))
    else:
        try:
            pedido.id_status = novoStatus.id
            db.session.commit()
            flash("Status atualizado com suscesso", "success")
            return redirect(url_for('pedidos.index'))
        except:
            db.session.rollback()
            flash("Erro ao atualizar o status")
            return redirect(url_for('pedidos.index'))

@pedidos.route('/pedidos/imprimirOrcamento/<id>', methods=['GET', 'POST'])
@login_required
def imprimirOrcamento(id):
    pedido = Pedido.query.filter_by(id=id).first_or_404()
    itens = Item.query.filter_by(id_pedido=id).all()    
    cliente = Usuario.query.filter_by(id=pedido.id_cliente).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    enderURL = str(cliente.endereco.endereco)+","+str(cliente.endereco.numero)+","+str(cliente.endereco.municipio)+"-"+str(cliente.endereco.uf)+","+str(cliente.endereco.pais)
    encodedURL = enderURL.replace(' ','+').replace(',','%2C')
    
    return render_template('pedidos/imprimirOrcamento.html', 
                        config = configuracao,
                        pedido = pedido,
                        enderURL = enderURL,
                        encodedURL = encodedURL,
                        itens = itens,
                        cliente = cliente,
                        dias = abs(datetime.now() - configuracao.validade).days
                        )

@pedidos.route('/pedidos/imprimir/<id>', methods=['GET', 'POST'])
@login_required
def imprimir(id):
    pedido = Pedido.query.filter_by(id=id).first_or_404()
    itens = Item.query.filter_by(id_pedido=id).all()
    cliente = Usuario.query.filter_by(id=pedido.id_cliente).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    enderURL = str(cliente.endereco.endereco)+","+str(cliente.endereco.numero)+","+str(cliente.endereco.municipio)+"-"+str(cliente.endereco.uf)+","+str(cliente.endereco.pais)
    encodedURL = enderURL.replace(' ','+').replace(',','%2C')
    
    
    if configuracao.tipoImpressao == True:
        return render_template('pedidos/imprimirTermica.html', 
                            config = configuracao,
                            pedido = pedido,
                            enderURL = enderURL,
                            encodedURL = encodedURL,
                            itens = itens,
                            cliente = cliente,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
    if configuracao.tipoImpressao == False:
        return render_template('pedidos/imprimir.html', 
                            config = configuracao,
                            pedido = pedido,
                            enderURL = enderURL,
                            encodedURL = encodedURL,
                            itens = itens,
                            cliente = cliente,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pedidos/entrega', methods=['GET', 'POST'])
@login_required
def entrega():
    pedido = Pedido.query.filter_by(id_status = 4).all()
    itens = Item.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    stat = status.query.all()
    
    return render_template('pedidos/entrega.html', 
                            config = configuracao,
                            pedidos = pedido,
                            st = stat,
                            itens = itens,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pedidos/cozinha', methods=['GET', 'POST'])
@login_required
def cozinha():
    pedido = Pedido.query.filter_by(id_status = 3).all()
    itens = Item.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    stat = status.query.all()
    
    return render_template('pedidos/cozinha.html', 
                            config = configuracao,
                            pedidos = pedido,
                            st = stat,
                            itens = itens,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/tabela', methods=['GET', 'POST'])
@login_required
def tabela():
    pedidos = Pedido.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    stat = status.query.all()
    clientes = Usuario.query.filter_by(id_perfilUsuario=6).all()
    usuarios = Usuario.query.all()

    pedidosArray = []
    for pedido in pedidos:
        pedidoObj = {}
        pedidoObj['id'] = pedido.id
        pedidoObj['dtCreate'] = pedido.dtCreate.strftime("%Y/%m/%d")
        pedidoObj['dtUpdate'] = pedido.dtUpdate.strftime("%Y/%m/%d")
        pedidoObj['subtotal'] = pedido.subtotal
        pedidoObj['desconto'] = pedido.desconto
        pedidoObj['frete'] = pedido.frete 
        pedidoObj['total'] = pedido.total
        pedidoObj['formaPagamento'] = pedido.formaPagamento
        pedidoObj['id_responsavel'] =  pedido.id_responsavel
        responsavel = Usuario.query.filter_by(id = pedido.id_responsavel).first_or_404()
        pedidoObj['nomeResponsavel'] =  responsavel.nome
        
        pedidoObj['id_cliente'] = pedido.id_cliente
        pedidoObj['id_entregador'] = pedido.id_entregador
        pedidoObj['id_status'] = pedido.status.id
        pedidoObj['nomeStatus'] = pedido.status.nome
        pedidoObj['corStatus'] = pedido.status.cor
        if pedido.id_entregador == '' or pedido.id_entregador is None:
            pedidoObj['nomeEntregador'] = 'Não atribuido'
        else:
            entregador = Usuario.query.filter_by(id = pedido.id_entregador).first_or_404()
            pedidoObj['nomeEntregador'] = entregador.nome

        clientePedido = Usuario.query.filter_by(id = pedido.id_cliente).first_or_404()
        pedidoObj['clienteNome'] = clientePedido.nome
        pedidoObj['clienteTelefone'] = clientePedido.telefone
        pedidoObj['clienteCelular'] = clientePedido.celular
        pedidoObj['clienteEmail'] = clientePedido.email
        pedidoObj['clienteEndereco'] = str(clientePedido.endereco.endereco)+","+str(clientePedido.endereco.numero)+","+str(clientePedido.endereco.municipio)+"-"+str(clientePedido.endereco.uf)+","+str(clientePedido.endereco.pais)
        enderURL = str(clientePedido.endereco.endereco)+","+str(clientePedido.endereco.numero)+","+str(clientePedido.endereco.municipio)+"-"+str(clientePedido.endereco.uf)+","+str(clientePedido.endereco.pais)
        pedidoObj['clienteUrlEndereco'] = enderURL.replace(' ','+').replace(',','%2C')
        
        pedidosArray.append(pedidoObj)

    return jsonify({'pedidos' : pedidosArray })
    

@pedidos.route('/pedidos', methods=['GET', 'POST'])
@login_required
def index():
    pedidos = Pedido.query.all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    stat = status.query.all()
    clientes = Cliente.query.filter_by(id_perfilUsuario=6).all()
    usuarios = Usuario.query.all()
    
    return render_template('pedidos/tabela.html', 
                            config = configuracao,
                            pedidos = pedidos,
                            st = stat,
                            clientes = clientes,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pdv', methods=['GET', 'POST'])
@login_required
def pdv():
    configuracao = config.query.filter_by(id=1).first_or_404()
    clienteConsulta = Cliente.query.filter_by(id_perfilUsuario = 6).all()
    produtosList = Estoque.query.all()
    categorias = Categoria.query.all()

    return render_template('pedidos/pdv.html', 
                            config = configuracao,
                            clientes = clienteConsulta,
                            produtos = produtosList,
                            categorias = categorias,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pdvSalvar', methods = ['POST'])
def pdvSalvar():   
    cont = 0
    Config = config.query.filter_by(id=1).first_or_404()
    if request.method == 'POST':
        #transportando a request para uma variavel isolada
        for key,val in request.form.items():
            result = key
        # print(result)
        # convertendo para um dicionario python
        meuJsonString = json.loads(result)

        for k in meuJsonString["cliente"]:
            cliente = k["id"]

        for k in meuJsonString["resumo"]:
            subTotal = k["subtotal"]
            frete = k["frete"]
            formasPagamento = k["pagamento"]
            total = k["total"]
            observacao = k["obs"]

        try:
            pedido = Pedido(
                id_cliente = cliente,
                dtCreate = datetime.utcnow(),
                dtUpdate = datetime.utcnow(),
                subtotal = subTotal,
                desconto = '0',
                frete = frete,
                total = total,                
                id_status = 2,
                formaPagamento = formasPagamento,
                observacao = observacao,
                id_responsavel = current_user.id
                )
            db.session.add(pedido)
            db.session.commit()
        except:
            db.session.rollback()
            flash("As informações do pedido não puderam ser salvas","danger")
            return redirect(url_for('pedidos.pdv'))
        
        for k in meuJsonString["itens"]:
            try:
                lista = Item(
                    id_pedido = pedido.id,
                    quantidade = k["quantidade"],
                    produto = k["nomeProduto"],
                    precoUnitario = k["preco"],    
                    precoTotal = k["total"],
                    id_estoque = k["id_estoque"]
                    )
                db.session.add(lista)
                db.session.commit()                
            except:
                db.session.rollback()
                flash("Item {0} não pode ser salvo".format(cont),"danger")
                return redirect(url_for('pedidos.pdv'))
            cont = cont + 1 
        
    if len(meuJsonString["itens"]) == cont:  
        params = { 
            '0': Config.imprimir,
            '1':'/pedidos/imprimir/{0}'.format(pedido.id),
            '2':'/pedidos',
            '3':'/pdv',
             }      
        return jsonify(params)
   
    return '0'

@pedidos.route('/pedidos/cadastroPedido', methods=['GET', 'POST'])
@login_required
def cadastroPedido():
    pForm = pedidoForm()
    cCliente = Cliente.query.filter_by(id_perfilUsuario = 6).all()
    cEstoque = Estoque.query.all()
    cont = 0
    meuJsonString = {}
    Config = config.query.filter_by(id=1).first_or_404() 

    if request.method == 'POST':
            #transportando a request para uma variavel isolada
        for key,val in request.form.items():
            result = key
        # print(result)
        # convertendo para um dicionario python
        meuJsonString = json.loads(result)

        for k in meuJsonString["cliente"]:
            cliente = k["id"]

        for k in meuJsonString["resumo"]:
            subTotal = k["subtotal"]
            frete = k["frete"]
            desconto = k["desconto"]
            formasPagamento = k["pagamento"]
            total = k["total"]
            observacao = k["obs"]

        try:
            pedido = Pedido(
                id_cliente = cliente,
                dtCreate = datetime.utcnow(),
                dtUpdate = datetime.utcnow(),
                subtotal = subTotal,
                desconto = desconto,
                frete = frete,
                total = total,                
                id_status = 2,
                formaPagamento = formasPagamento,
                observacao = observacao,
                id_responsavel = current_user.id
                )
            db.session.add(pedido)
            db.session.commit()
        except:
            db.session.rollback()
            flash("As informações do pedido não puderam ser salvas","danger")
            return redirect(url_for('pedidos.cadastroPedido'))
        
        for k in meuJsonString["itens"]:
            try:
                lista = Item(
                    id_pedido = pedido.id,
                    quantidade = k["quantidade"],
                    produto = k["nomeProduto"],
                    precoUnitario = k["preco"],    
                    precoTotal = k["total"]
                    )
                db.session.add(lista)
                db.session.commit()                
            except:
                db.session.rollback()
                flash("Item {0} não pode ser salvo".format(cont),"danger")
                return redirect(url_for('pedidos.cadastroPedido'))
            cont = cont + 1 
        
        if len(meuJsonString["itens"]) == cont:  
            params = { 
                '0': Config.imprimir,
                '1':'/pedidos/imprimir/{0}'.format(pedido.id),
                '2':'/pedidos',
                '3':'/pedidos/cadastroPedido',
                }      
            return jsonify(params)        

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('pedidos/cadastroPedido.html', 
                            config = configuracao,
                            form = pForm,
                            clientes = cCliente,
                            produtos = cEstoque,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pedidos/visualizar/<id>', methods=['GET', 'POST'])
@login_required
def visualizarPedido(id):
    pedido = Pedido.query.filter_by(id=id).first_or_404()
    itens = Item.query.filter_by(id_pedido=id).all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    enderURL = str(pedido.cliente.endereco.endereco)+","+str(pedido.cliente.endereco.numero)+","+str(pedido.cliente.endereco.municipio)+"-"+str(pedido.cliente.endereco.uf)+","+str(pedido.cliente.endereco.pais)
    encodedURL = enderURL.replace(' ','+').replace(',','%2C')
    
    return render_template('pedidos/visualizarPedido.html', 
                            config = configuracao,
                            pedido = pedido,
                            enderURL = enderURL,
                            encodedURL = encodedURL,
                            itens = itens,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pedidos/editar/<id>', methods=['GET', 'POST'])
@login_required
def editarPedido(id):
    cont = 0

    Config = config.query.filter_by(id=1).first_or_404()

    if request.method == 'POST':
         #transportando a request para uma variavel isolada
        for key,val in request.form.items():
            result = key
        # convertendo para um dicionario python
        meuJsonString = json.loads(result)
        pedidoOld = Pedido.query.filter_by(id=id).first_or_404() 
        itensOld = Item.query.filter_by(id_pedido=id).all()
        for k in meuJsonString["cliente"]:
            pedidoOld.id_cliente = k["id"]

        
        pedidoOld.dtUpdate = datetime.utcnow()

        for k in meuJsonString["resumo"]:
            pedidoOld.subtotal = k["subtotal"]
            pedidoOld.frete = k["frete"]
            pedidoOld.desconto = k["desconto"]
            pedidoOld.formasPagamento = k["pagamento"]
            pedidoOld.id_status = k["status"]
            pedidoOld.total = k["total"]
            pedidoOld.observacao = k["obs"]
        
        for item in itensOld:
            try:
                db.session.delete(item)
                db.session.commit()
            except:
                db.session.rollback()
                flash('Item não foi excluido', 'warning')
                return redirect(url_for('pedidos.index'))

        for k in meuJsonString["itens"]:
            try:
                lista = Item(
                    id_pedido = pedidoOld.id,
                    quantidade = k["quantidade"],
                    produto = k["nomeProduto"],
                    precoUnitario = k["preco"],    
                    precoTotal = k["total"]
                    )
                db.session.add(lista)
                db.session.commit()                
            except:
                db.session.rollback()
                flash("Item {0} não pode ser salvo".format(cont),"danger")
                return redirect(url_for('pedidos.cadastroPedido'))
            cont = cont + 1 
        
        if len(meuJsonString["itens"]) == cont:  
            params = { 
                '0': Config.imprimir,
                '1':'/pedidos/imprimir/{0}'.format(pedidoOld.id),
                '2':'/pedidos',
                '3':'/pedidos/cadastroPedido',
                }      
            return jsonify(params)


    pForm = pedidoForm()
    cCliente = Cliente.query.all()
    cEstoque = Estoque.query.all()
    pedido = Pedido.query.filter_by(id=id).first_or_404()    
    itens = Item.query.filter_by(id_pedido=id).all()
    pForm.observacao.data = pedido.observacao
    
    pForm.statusPedido.choices = [(pedido.status.id,pedido.status.nome)]
    allStatus = status.query.all()
    for stat in allStatus:
        pForm.statusPedido.choices += [(stat.id,stat.nome)]
    
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('pedidos/editarPedido.html', 
                            form = pForm,
                            config = configuracao,
                            pedido = pedido,
                            itens = itens,                            
                            clientes = cCliente,
                            produtos = cEstoque,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@pedidos.route('/pedidos/excluir/<id>', methods=['GET', 'POST'])
@login_required
def excluirPedido(id):
    pedido = Pedido.query.filter_by(id=id).first_or_404()
    itens = Item.query.filter_by(id_pedido=id).all()
    configuracao = config.query.filter_by(id=1).first_or_404()
    enderURL = str(pedido.cliente.endereco.endereco)+","+str(pedido.cliente.endereco.numero)+","+str(pedido.cliente.endereco.municipio)+"-"+str(pedido.cliente.endereco.uf)+","+str(pedido.cliente.endereco.pais)
    encodedURL = enderURL.replace(' ','+').replace(',','%2C')
    cForm = confirmForm()

    if cForm.n.data == True and request.method == 'POST':
        flash('Pedido nao foi excluido', 'warning')
        return redirect(url_for('pedidos.index'))
    
    if cForm.s.data == True and request.method == 'POST':
        for item in itens:
            try:
                db.session.delete(item)
                db.session.commit()
            except:
                db.session.rollback()
                flash('Item não foi excluido', 'warning')
                return redirect(url_for('pedidos.index'))
        try:
            db.session.delete(pedido)
            db.session.commit()
            flash('Pedido excluido com sucesso', 'success')
            return redirect(url_for('pedidos.index'))
        except:
            db.session.rollback()
            flash('O pedido não foi excluido', 'warning')
            return redirect(url_for('pedidos.index'))
    
    return render_template('pedidos/excluirPedido.html', 
                            config = configuracao,
                            pedido = pedido,
                            enderURL = enderURL,
                            encodedURL = encodedURL,
                            itens = itens,
                            form = cForm,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )
