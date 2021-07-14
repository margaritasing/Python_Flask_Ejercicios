import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

gestor = LoginManager() #esta es la instancia de LoginManager, valida que es usuario esta loggado
app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta' #creamos la clave secreta

directorio = os.path.abspath(os.path.dirname(__file__)) #directorio del trabajo de la aplicacion
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'loginbd.sqlite')#configurar la ruta de nuestra db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #esta es la parte de base de datos

basededatos = SQLAlchemy(app) #une la aplicacion con la base de datos
Migrate(app,basededatos) #conectamos, para poder migrarlo

gestor.init_app(app) # configuramos el init app
gestor.login_view = 'login' #
