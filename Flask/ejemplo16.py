from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
directorio = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'personas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basededatos = SQLAlchemy(app)
Migrate(app, basededatos)

api = Api(app)

class PersonaBD(basededatos.Model):
    __tablename__ = 'Personas'
    nombre = basededatos.Column(basededatos.String(100),primary_key=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def json(self):
        return{'nombre':self.nombre}



class Personas(Resource):
    def get(self,valor):
        persona = PersonaBD.query.filter_by(nombre=valor)
        if persona:
            return persona.json()
        return{'resultado': 'Persona no existe en la db'}

    def post(self,valor):
        persona = PersonaBD(nombre=valor)
        basededatos.session.add(persona)
        basededatos.session.commit()
        return{'respuesta':'Persona añadida'}

    def delete(self, valor):
        persona = PersonaBD.query.filter_by(nombre=valor).first()
        basededatos.session.delete(persona)
        basededatos.session.commit()
        return{'respuesta':'Persona borrada'}

class Listar(Resource):
    def get(self):
        persona = PersonaBD.query.all()
        listas_personas =[persona.json() for persona in personas]
        return{'resultado': listas_personas}

api.add_resource(Personas, '/persona/<string:valor>')
api.add_resource(Listar, '/listar')

if __name__ == '__main__':
    app.run(debug=True)
