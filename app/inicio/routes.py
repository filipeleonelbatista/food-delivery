from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from app import db
from app.inicio.forms import InicioForm, viewForm
from . import inicio

from ..models import config, endereco, Estoque, View, InicioView, Usuario, Cliente, Item, Pedido, Categoria, perfilUsuario, status

from datetime import datetime

@inicio.route('/pagina-inicial')
@login_required
def index():
    view = InicioView.query.filter_by(id = current_user.id_inicioview).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    estoque = Estoque.query.all()
    users = Usuario.query.all()    
    clientes = Cliente.query.filter_by(id_perfilUsuario = 6).all()
    pedidos = Pedido.query.all()
    form = InicioForm()

    ganhoDiario = 0.00    
    ganhoMensal = 0.00 
    pedidosDiaConcluidos = 0 
    pedidosDia = 0 
    #Encontrar o mes da data
    data = datetime.utcnow()
    dtInicial = datetime.strptime("1/"+str(data.month)+"/"+str(data.year),"%d/%m/%Y")
    if data.month == 2:
        if data.year % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            dtFinal = datetime.strptime("29/"+str(data.month)+"/"+str(data.year),"%d/%m/%Y")
        else:
            dtFinal = datetime.strptime("28/"+str(data.month)+"/"+str(data.year),"%d/%m/%Y")
    else:
        if data.month == 4 or data.month == 6 or data.month == 9 or data.month == 11:
            dtFinal = datetime.strptime("30/"+str(data.month)+"/"+str(data.year),"%d/%m/%Y")
        else:
            if data.month == 1 or data.month == 3 or data.month == 5 or data.month == 7 or data.month == 8 or data.month == 10 or data.month == 12:
                dtFinal = datetime.strptime("31/"+str(data.month)+"/"+str(data.year),"%d/%m/%Y")

    

    for pedido in pedidos:
        if pedido.status.id == 5 or pedido.status.id > 5 :
            if pedido.dtUpdate.strftime("%d/%m/%Y") == datetime.utcnow().strftime("%d/%m/%Y"):
                ganhoDiario = ganhoDiario + float(pedido.total)
            if pedido.dtUpdate >= dtInicial and pedido.dtUpdate <= dtFinal:
                ganhoMensal = ganhoMensal + float(pedido.total)
            pedidosDiaConcluidos = pedidosDiaConcluidos + 1

        if pedido.dtUpdate.strftime("%d/%m/%Y") == datetime.utcnow().strftime("%d/%m/%Y"):
            pedidosDia = pedidosDia + 1


    stat = status.query.all()
    
    form.selecionaGrafico.choices = []
    form.selecionaGrafico.choices += [("0","Todos")]
    for st in stat:
        form.selecionaGrafico.choices += [( st.id, st.nome)]
    
    form.selecionaSemanas.choices = []
    form.selecionaSemanas.choices += [("0","Todos")]
    for sem in range(1, 53):
        form.selecionaSemanas.choices += [( sem, sem)]
    
    form.responsavel.choices = []
    form.responsavel.choices += [("0","Todos")]
    for resp in users:
        if resp.id != 1 and resp.id < 6:
            form.responsavel.choices += [(resp.id,resp.nome)]

    if pedidosDia == 0:
        pedidosDia = 1    
    return render_template('inicio/index.html', 
                            form = form,
                            config = configuracao,
                            estoque = estoque,
                            funcionarios = users,
                            clientes = clientes,
                            pedidos = pedidos,
                            view = view,
                            ganhoDiario = "{0:.2f}".format(ganhoDiario),
                            ganhoMensal = "{0:.2f}".format(ganhoMensal),
                            pedidosDia = pedidosDia,
                            pedidosDiaConcluidos = pedidosDiaConcluidos,
                            percentualPedidos = (pedidosDiaConcluidos*100)/pedidosDia,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@inicio.route('/pagina-inicial/selecionarRelatorios', methods=['GET', 'POST'])
@login_required
def editarView():
    view = InicioView.query.filter_by(id = current_user.id_inicioview).first_or_404()
    form = viewForm()
    

    if form.cancelar.data == True and request.method == 'POST':
        flash("Nada foi alterado", "warning")
        return redirect(url_for('inicio.index'))
    
    if form.salvar.data == True and request.method == 'POST':
        if view:
            view.cliente = form.cliente.data
            view.funcionario = form.funcionario.data
            view.pedido = form.pedido.data
            view.estoque = form.estoque.data
            view.graficoPedidos = form.graficoPedidos.data
            try:
                db.session.commit()
                flash("Relatórios selecionados com sucesso!", "success")
                return redirect(url_for('inicio.index'))
            except:
                db.session.rollback()
                flash("Erro ao selecionar os relatórios", "danger")
                return redirect(url_for('inicio.index'))

    
    configuracao = config.query.filter_by(id=1).first_or_404()
    return render_template('inicio/editarViews.html', 
                            form = form,
                            config = configuracao,
                            view = view,
                            dias = abs(datetime.now() - configuracao.validade).days
                            )

@inicio.route('/pagina-inicial/sql')
@login_required
def donwloadsql():
    
    from flask import send_file   
    
    import os

    if os.name == 'nt':
        path = os.getcwd()+'\\data-dev.sqlite'
    else:
        path = os.getcwd()+'/data-dev.sqlite'
    
    return send_file(path, as_attachment=True)

@inicio.route('/ferramentas/vcard', methods=['GET', 'POST'])
@login_required
def vcard():
    import os

    if os.name == 'nt':
        path = os.getcwd()+'\\app\\static\\vcards\\'
    else:
        path = os.getcwd()+'/app/static/vcards/'

    meuperfil = Usuario.query.filter_by(id=current_user.id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()
    

    nomeArq = (meuperfil.nome.replace(" ","-")+".vcf")
    url = request.base_url
    url = url.replace('ferramentas/vcard','static/vcards/'+str(nomeArq))
    
    f= open(path+nomeArq,"w+")
    url2 = url.replace('static/vcards/'+str(nomeArq),'')
    vcard = []
    vcard.append('BEGIN:VCARD\n')
    vcard.append('VERSION:3.0\n')
    vcard.append('N:'+str(meuperfil.nome)+';\n')
    vcard.append('\nORG:'+str(configuracao.nomeFantasia))
    vcard.append('\nTITLE:'+str(meuperfil.perfilUsuario.nome))
    vcard.append('\nTEL;TYPE=WORK:'+str(configuracao.telefone))
    vcard.append('\nURL:'+str(url2))
    vcard.append('\nTEL;TYPE=HOME:'+str(meuperfil.celular))
    vcard.append('\nEMAIL:'+str(meuperfil.email))
    vcard.append('\nEND:VCARD')
    f.writelines(vcard)
    f.close()

    
    return render_template('inicio/vcard.html', meuPerfil = meuperfil, 
                                                config = configuracao, 
                                                url = url,
                                                dias = abs(datetime.now() - configuracao.validade).days
                                                )


@inicio.route('/ferramentas/geradorAssinaturas', methods=['GET', 'POST'])
@login_required
def geradorAssinaturas():
    meuperfil = Usuario.query.filter_by(id=current_user.id).first_or_404()
    configuracao = config.query.filter_by(id=1).first_or_404()

    
    return render_template('inicio/gerador.html', meuPerfil = meuperfil, 
                                                config = configuracao,
                                                dias = abs(datetime.now() - configuracao.validade).days
                                                )
