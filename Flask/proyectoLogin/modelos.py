from proyectoLogin import basededatos,gestor # permite importar de la carpeta esta clases
from werkzeug.security import generate_password_hash, check_password_hash # permite imprtar dos clases y funciones
from flask_login import UserMixin #

@gestor.user_loader # permite definir o cargar el usuario actual
def load_user(Usuario_id): #permite recoger de la db el usuaiio y si esta logado,
    return Usuario.query.get(Usuario_id) # recogelo en memoria, lo cual nos permite conocer quien
                                         # es el usuaiio que esta loggeado en ese momento
class Usuario(basededatos.Model, UserMixin): # creamos la clase usuario, y esta hereda de base de datos y de otra clase UserMixin
    __tablename__ = 'usuarios' # nombre de la tabla
    id = basededatos.Column(basededatos.Integer, primary_key=True) #columnas de la db, y su tipo de datos
    email = basededatos.Column(basededatos.String(64), unique=True, index=True)
    nombre = basededatos.Column(basededatos.String(64), unique=True, index=True)
    password_encriptada = basededatos.Column(basededatos.String(128))

    def __init__(self,email,nombre,password): #funciones del contructor, se le pasa 3 parametros
        self.email = email
        self.nombre = nombre
        self.password_encriptada = generate_password_hash(password) #para generar la passwoord que pasa lee usuario y guardarla en la db

    def verificar_password(self,password): #
        return check_password_hash(self.password_encriptada,password) # verifica la clave , si es correcta
