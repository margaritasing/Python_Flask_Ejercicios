import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))
print(directorio)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)

migrate = Migrate(app.basededatos)
# Creacion del modelo a base de datos
class Persona(basededatos.Model):
    __tablaname__ = 'Persona'

    id = basededatos.Column(basededatos.Integer, primary_key = True)
    nombre = basededatos.Column(basededatos.Text)
    edad = basededatos.Column(basededatos.Integer)
    color = basededatos.Column(basededatos.Text)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.color = color
#la maldita base de datos no quier funcionar...
        # with app.app_context(): appbuilder.init_app(app, db.session)

    def __repr__(self):
        texto = "Persona: nombre={} , edad={} y color={}".format(self.nombre, self.edad, self.color)
        return texto
