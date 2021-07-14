from proyectoLogin import app, basededatos
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from proyectoLogin.modelos import Usuario
from proyectoLogin.formulario import Formulario_Registro, Formulario_Login
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/bienvenido')
@login_required
def bienvenido():
    return render_template('bienvenido.html')

@app.route('/salir')
@login_required
def salir():
    logout_user()
    flash('Sección finlizada')
    return redirect(url_for('principal'))

@app.route('/entrar', methods=['GET','POST']) # si el usuario entra
def entrar():
    formulario = Formulario_Login() # solicita el mail y password
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formulario.email.data).first() # se recoge el usuario que tenga ese mail
        if usuario is not None:
            if check_password_hash(usuario.password_encriptada, formulario.password.data):# si es correcta se hace el login del usuario
                login_user(usuario) #permite darle alta de una session al Usuario
                flash("Usuario entro correctamente")
                proxima = request.args.get('next') # redirige al usuario a un vista x
                if proxima == None or not next[0] == '/':
                    proxima = url_for('bienvenido') # se coloca un valor por defecto, en caso de que next no recupere algun informacion de la ruta del usuario
                return redirect(proxima)
    return render_template('entrar.html', formulario=formulario) # si el Usuario mo se enmvio se utiliza esta pagina por defecto

@app.route('/registrar', methods=['GET','POST']) # tomamos los datos que esta en el registro y los guardamos en db
def registrar():
    formulario = Formulario_Registro() # se registran los datos, esta clase esta definida en otro archivo
    if formulario.validate_on_submit():
        usuario = Usuario(email=formulario.email.data, nombre= formulario.nombre.data,
                          password= formulario.password.data)
        basededatos.session.add(usuario)
        basededatos.session.commit()
        flash('Usuario registrado correctamente')
        return redirect(url_for('entrar'))
    return render_template('registrar.html', formulario=formulario) # en caso de que no se envie ponemos la pagina de registrar


if __name__ == '__main__':
    app.run(debug=True)
