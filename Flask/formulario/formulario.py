from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class FormularioAlta(FlaskForm):
    nombre = StringField('Nombre de la mascota: ')
    boton = SubmitField('Añadir')

class FormularioBaja(FlaskForm):
    id = IntegerField('Identificador de la mascota: ')
    boton = SubmitField('Borrar')
