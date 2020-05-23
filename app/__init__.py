from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_datepicker import datepicker

bootstrap = Bootstrap
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

Datepicker = datepicker
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    from .loja import loja as loja_blueprint
    app.register_blueprint(loja_blueprint)

    from .install import install as install_blueprint
    app.register_blueprint(install_blueprint)
    
    from .inicio import inicio as inicio_blueprint
    app.register_blueprint(inicio_blueprint)

    from .estoque import estoque as estoque_blueprint
    app.register_blueprint(estoque_blueprint)

    from .pedidos import pedidos as pedidos_blueprint
    app.register_blueprint(pedidos_blueprint)

    from .usuarios import usuarios as usuarios_blueprint
    app.register_blueprint(usuarios_blueprint)
    
    from .configuracao import configuracao as configuracao_blueprint
    app.register_blueprint(configuracao_blueprint)
    # Inicializando app Bootstrap
    bootstrap(app)

    # Inicializando app datepicker
    Datepicker(app)

    # Inicializando Database
    db.init_app(app)
    
    # Inicializando Autenticacao
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    login_manager.init_app(app)

    return app



