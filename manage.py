#!/usr/bin/env python
import os

from flask_migrate import Migrate, MigrateCommand

from app import create_app
from flask_script import Manager
from app import db
from app.models import config, endereco, Estoque, View, InicioView, Usuario, Item, Pedido, perfilUsuario

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def createDb():
    db.create_all()
    print('Banco criado') 

@manager.command
def adduser(nome, cpf, admin=True):
    """ Registr um novo usuário """
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt="Confirme: ")
    if password != password2:
        import sys
        sys.exit('Erro: senhas nao conferem')
    db.create_all()
    
    Config = config()  
    inicioview = InicioView()
    view = View()
    Endereco = endereco()
    user = Usuario(nome=nome, CPF=cpf, password=password, is_admin=admin)

    db.session.add(Config)
    db.session.commit()
    db.session.add(inicioview)
    db.session.commit()
    db.session.add(view)
    db.session.commit()
    db.session.add(Endereco)
    db.session.commit()
    db.session.add(user)
    db.session.commit()
    
    print('Usuario {0} foi registrado com sucesso.'.format(cpf) )

if __name__ == '__main__':
    manager.run()


