from flask import Flask, render_template, request


app = Flask(__name__)

@app.get('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.get('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.get('/formulario')
def formulario():
    return render_template('formulario.html')

@app.get('/gracias')
def gracias():
    valor1 = request.args.get('nombre')
    valor2 = request.args.get('apellido')
    return render_template('gracias.html', nombre=valor1, apellido=valor2)


@app.get('/nombre')
def nombre():
    return render_template('nombre.html')

@app.get('/resultado')
def resultado():
    nombre = request.args.get('nombre')
    minuscula = any(letra.islower() for letra in nombre)
    numero = any(letra.isdigit() for letra in nombre)
    mayuscula= nombre[0].isupper()
    todo = minuscula and numero and mayuscula
    return render_template('resultado.html', todo=todo, minuscula=minuscula,
                           mayuscula=mayuscula, numero=numero)


@app.errorhandler(404)
def error_404(e):
    return render_template('pagina404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
