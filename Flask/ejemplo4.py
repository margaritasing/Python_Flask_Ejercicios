from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'clavesecreta'

class Formulario(FlaskForm):
    nombre = StringField("Nombre")
    enviar = SubmitField("Enviar")

@app.route("/", methods=["GET", "POST"])
def principal():
    nombre =  ''
    enviado = False
    formulario = Formulario()

    if formulario.validate_on_submit():
        enviado= True
        nombre = formulario.nombre.data
        formulario.nombre.data = ''

    return render_template('index.html', nombre= nombre, enviado=enviado, formulario=formulario)

if __name__ == '__main__':
    app.run(debug = True)
