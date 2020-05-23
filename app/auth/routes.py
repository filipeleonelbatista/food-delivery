import os
from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm
from datetime import datetime, timedelta

from app import db

from pyUFbr.baseuf import ufbr

from . import auth
from ..models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, Categoria, perfilUsuario

@auth.route('/atualizacao/u=<usuario>&s=<senha>&m=<mensagem>', methods=['GET', 'POST'])
def atualiza(usuario, senha, mensagem):
    usr = Usuario.query.filter_by(CPF = usuario).first()

    Config = config.query.filter_by(id=1).first()
    if Config is None:
        return -1
    
    if usr.perfilUsuario.id > 6:
        return -1
            
    if usr is None or not usr.verify_password(senha):
        return -1
    
    
    Config.update = True
    Config.sobreUpdate = mensagem
    try:
        db.session.commit()
        return "Erro"
    except:
        db.session.rollback()
        return "Ok"
    
    configuracao = config.query.filter_by(id=1).first_or_404()
    return mensagem

@auth.route('/validacao/u=<usuario>&s=<senha>', methods=['GET', 'POST'])
def revalida(usuario, senha):  
    usr = Usuario.query.filter_by(CPF = usuario).first()

    Config = config.query.filter_by(id=1).first()
    if Config is None:
        return -1
    
    if usr.perfilUsuario.id > 6:
        return -1
            
    if usr is None or not usr.verify_password(senha):
        return -1
    mes = 0
    validadeNova = datetime.now()
    if validadeNova.month == 12:
        mes = 1
    else:
        mes = validadeNova.month + 1

    if Config.ativa == False:
        if usr.perfilUsuario.id == 1:
            validadeNova = datetime.now()
            Config.ativa = True
            Config.validade = datetime.strptime(str(validadeNova.day)+"/"+str(mes)+"/"+str(validadeNova.year),"%d/%m/%Y")
            try:
                db.session.commit()
                return 0
            except:
                db.session.rollback()
                return -1
        else:    
            return -1


    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return "Ok"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    Config = config.query.filter_by(id=1).first()
    if Config is None:
        return redirect(url_for('install.index'))
    
    if current_user.is_authenticated:
        if current_user.perfilUsuario.id == 6:
            return redirect(url_for('loja.index'))
        else:
            return redirect(url_for('inicio.index'))
            
    form = LoginForm()   

    if form.submit.data:
        user = Usuario.query.filter_by(CPF=form.cpf.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Cpf digitado ou Senha Inválidos', 'danger')
            return redirect(url_for('.login'))
        login_user(user, form.remember_me.data)
        if Config.ativa == False:
            if current_user.perfilUsuario.id == 1:
                flash('O Sistema está desativado!', 'danger')
                return redirect(url_for('inicio.index'))
            else:                
                flash('Sistema expirado, contato o Administrador', 'danger')
                logout_user()
                return redirect(url_for('auth.login'))

        if current_user.perfilUsuario.id == 6:
            return redirect(url_for('loja.index'))
        else:
            
            if abs(datetime.now() - Config.validade).days < 3:
                return redirect(request.args.get('next') or url_for('auth.valida'))
            else:
                return redirect(request.args.get('next') or url_for('inicio.index'))


    configuracao = config.query.filter_by(id=1).first_or_404()
    
    return render_template('auth/login.html', form=form, config = configuracao, now = datetime.utcnow(),
                            dias = abs(datetime.now() - configuracao.validade).days)

@auth.route('/validacao')
@login_required
def valida():    
    cfg = config.query.filter_by(id=1).first_or_404()
    if abs(datetime.now() - cfg.validade).days == 0:
        cfg.ativa = False
        try:
            db.session.commit()
            flash('O serviço foi desativado.', 'warning')
            logout_user()
            return redirect(url_for('auth.login'))
        except:
            db.session.rollback()
            flash('Não foi possivel atualizar as informações da empresa.', 'danger')

    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('auth/valida.html', config = configuracao,
                            dias = abs(datetime.now() - configuracao.validade).days)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Voce foi desconectado.', 'warning')
    return redirect(url_for('.login'))

@auth.route('/municipios/<estado>', methods=['GET', 'POST'])
def municipios(estado):
    cities = []
    count=0
    for valor in ufbr.list_cidades(estado):
        cities += [(count, valor)]
        count=count+1

    cityArray = []

    for city in cities:
        cityObj = {}
        # cityObj['id'] = city[0]
        cityObj['id'] = city[1]
        cityObj['name'] = city[1]
        cityArray.append(cityObj)
    
    return jsonify({'municipios' : cityArray })

@auth.route('/relatorios/pedidos/s=<s>;d1=<d1>;d2=<d2>;r=<r>;', methods=['GET', 'POST'])
def relatoriosPedidos(s,d1,d2,r):
    
    if int(s) == 0 and int(r) == 0:
        
        pedidos = Pedido.query.all()    
    if int(s) > 0 and int(r) == 0:
        pedidos = Pedido.query.filter_by(id_status = int(s))
    if int(s) == 0 and int(r) > 0:
        pedidos = Pedido.query.filter_by(id_vendedor = int(r))
    if int(s) > 0 and int(r) > 0:
        pedidos = Pedido.query.filter_by(id_vendedor = int(r), id_status = int(s))

    if d1 == '0' and d2 == '0':
        temData = 0
    if d1 != '0' and d2 == '0':
        newInicialData = datetime.strptime(d1.replace('-','/'), "%d/%m/%Y")
        newFinalData = datetime.strptime(datetime.now().strftime("%d/%m/%Y"), "%d/%m/%Y")
        temData = 1
    if d1 == '0' and d2 != '0':
        temData = 0
    if d1 != '0' and d2 != '0':
        newInicialData = datetime.strptime(d1.replace('-','/'), "%d/%m/%Y")
        newFinalData = datetime.strptime(d2.replace('-','/'), "%d/%m/%Y")
        temData = 1
        
    #formação do json com os dados
    pedidoArray = []
    for pedido in pedidos:
        if temData == 0:
            pedidoObj = {}
            pedidoObj['id'] = pedido.id
            pedidoObj['cliente'] = pedido.cliente.nome
            pedidoObj['valor'] = pedido.total     
            pedidoObj['dataUpdate'] = pedido.dtUpdate.weekday() 
            pedidoObj['dataUpdateReal'] = pedido.dtUpdate.strftime("%Y-%m-%d")
            pedidoObj['dataUpdateReal2'] = pedido.dtUpdate.strftime("%d/%m/%Y")
            pedidoArray.append(pedidoObj)
        if temData == 1:
            if pedido.dtUpdate >= newInicialData and pedido.dtUpdate <= newFinalData:
                pedidoObj = {}
                pedidoObj['id'] = pedido.id
                pedidoObj['cliente'] = pedido.cliente.nome
                pedidoObj['valor'] = pedido.total     
                pedidoObj['dataUpdate'] = pedido.dtUpdate.weekday() 
                pedidoObj['dataUpdateReal'] = pedido.dtUpdate.strftime("%Y-%m-%d")
                pedidoObj['dataUpdateReal2'] = pedido.dtUpdate.strftime("%d/%m/%Y")
                pedidoArray.append(pedidoObj)

    return jsonify({'pedidos' : pedidoArray })


@auth.route('/relatorios/ganhos/<s>', methods=['GET', 'POST'])
def ganhos(s):
    if int(s) == 1:
        # ganhos diarios 
        pedidos = Pedido.query.filter_by(dtCreate = datetime.now())

    if int(s) == 2:
        # ganhos mensais 
        pedidos = Pedido.query.all()  

        pedidoArray = []
        for pedido in pedidos:
            if pedido.dtCreate >= (datetime.now() - timedelta(30)) and pedido.dtCreate <= datetime.now() :                
                pedidoObj = {}
                pedidoObj['idPedido'] = pedido.id
                pedidoObj['label'] = pedido.dtCreate.strftime("%d/%m/%Y")
                pedidoObj['data'] = pedido.total 
                pedidoArray.append(pedidoObj)       

        return jsonify(pedidoArray)


    if int(s) == 3:
        # ganhos totais
        pedidos = Pedido.query.all()   
        
    #formação do json com os dados
    pedidoArray = []
    for pedido in pedidos:
        pedidoObj = {}
        pedidoObj['idPedido'] = pedido.id
        pedidoObj['label'] = pedido.dtCreate.strftime("%d/%m/%Y")
        pedidoObj['data'] = pedido.total 
        pedidoArray.append(pedidoObj)
       

    return jsonify(pedidoArray)

