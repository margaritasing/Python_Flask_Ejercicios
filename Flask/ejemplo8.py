import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
migrate = Migrate(app, db)

directorio = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'mascotas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

class Mascota(basededatos.Model):  #el modelo de la base de datos se realizao con el modelo de la base de datos
    __tablename__ = 'Mascotas'     # una mascota puede tener un propietario
    id = basededatos.Column(basededatos.Integer, primary_key=True) #esta es l clave primaria, la cual servira como llave foranea para relacionar las tablas
    nombre = basededatos.Column(basededatos.Text) #Cada uno de los campos que contendra la tabla mascotas
    juguetes = basededatos.relationship('Juguete',backref='mascota',lazy='dynamic') #donde se establace que la clase mascota tendra una relacion con las clases juguetes y propietarios
    Propietario = basededatos.relationship('Propietario',backref='mascota',uselist=False)

    def __init__(self,nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = "Mascota : nombre {}".format(self.nombre) #referencia de la clase
        return texto

    def mostrar_juguetes(self):
        for juguete in self.juguetes: #muestralos juguetes que son propiedad de la mascota
            print(juguete.nombre)



class Juguete(basededatos.Model):
    __tablename__ = 'Juguetes'
    id = basededatos.Column(basededatos.Integer, primary_key = True) #, la clave primaria de la primera se relaciona como clave foranea para las otras
    nombre = basededatos.Column(basededatos.Text)
    mascota_id = basededatos.Column(basededatos.Integer, basededatos.ForeignKey('Mascotas.id'))# la clave primaria de la primera se relaciona como clave foranea para las otras

    def __init__(self,nombre,mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id


class Propietario(basededatos.Model):
    __tablename__ = 'Propietarios'
    id = basededatos.Column(basededatos.Integer, primary_key=True)
    nombre = basededatos.Column(basededatos.Text)
    mascota_id = basededatos.Column(basededatos.Integer, basededatos.ForeignKey('Mascotas.id')) #aqui se relaciona como clave foranea

    def __init__(self,nombre,mascota_id):
        self.nombre = nombre
        self.mascota_id = mascota_id
