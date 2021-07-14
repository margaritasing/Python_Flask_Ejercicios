from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField #importa lo datos que le vamos a solicitar al usuario
from wtforms.validators import DataRequired, Email, EqualTo # esto valida al usuario cuando se loggea
from wtforms import ValidationError # maneja las excepciones, cuando el usuario ya esta registrado y se registra nuevamente

class Formulario_Registro(FlaskForm): # son los campos que preguntaremos al usuario cuando este se registre
    email = StringField('Email',validators=[DataRequired(),Email()]) #validators, nos permite validar los campos, para que verifique que estos son correctos
    nombre = StringField('Nombre',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_repetir',message="Las password no coinciden")])
    password_repetir = PasswordField('Repetir password',validators=[DataRequired()])
    boton = SubmitField('Registrar')

    def verificar_mail(self,parametro): #lanza el mensajes de error, si el usuario ya esta registrado en la db
        if Usuario.query.filter_by(email=parametro.data).first():
            raise ValidationError('Error. Este mail ya ha sido utilizado')

    def verificar_nombre(self,parametro): #lanza mensajes de error si el nick del usuario ya se esta usando
        if Usuario.query.filter_by(nombre=parametro.data).first():
            raise ValidationError('Error. Este nombre ya ha sido utilizado')

class Formulario_Login(FlaskForm): #valida este formato
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    boton = SubmitField('Entrar')
