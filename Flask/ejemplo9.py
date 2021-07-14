import os
from formulario import FormularioAlta, FormularioBaja
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directorio = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'gestion_mascotas.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


basededatos = SQLAlchemy(app)

Migrate(app,basededatos)

class Mascota(basededatos.Model): #crea la tabla mas mascota en la base de datos
    __tablename__ = 'Mascotas'
    id = basededatos.Column(basededatos.Integer, primary_key = True)
    nombre = basededatos.Column(basededatos.Text)

    def __init__(self,nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = " Mascota : nombre {}".format(self.nombre)
        return texto

# vistas o rutas de la aplicacion
@app.route('/')
def principal():
    return render_template('vista_principal.html')

@app.route('/lista')
def lista():
    mascotas = Mascota.query.all()
    return render_template('vista_lista.html',mascotas=mascotas)

@app.route('/alta',methods=['GET','POST'])
def alta():
    formulario = FormularioAlta() #esta clase esta en el archivo formulario.py
    if formulario.validate_on_submit(): # guarda en base da datos la mascota
        nombre = formulario.nombre.data
        mascota = Mascota(nombre)
        basededatos.session.add(mascota)
        basededatos.session.commit()

        return redirect(url_for('lista')) # cundo haya echo todo lo anterior, mostrrara todas las mastocas en base de datos

    return render_template('vista_alta.html',formulario=formulario) # le pasamos la vista, le pasamos la variable formulario

@app.route('/borrar',methods=['GET','POST'])
def borrar():
    formulario = FormularioBaja() #del archivo formulario.py se estrae esta clase
    if formulario.validate_on_submit():# borra una mascota de lsa base de datos
        id = formulario.id.data
        mascota_borrar = Mascota.query.get(id)
        basededatos.session.delete(mascota_borrar)
        basededatos.session.commit()

        return redirect(url_for('lista'))

    return render_template('vista_borrar.html',formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
