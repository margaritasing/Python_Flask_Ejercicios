from flask import Flask #importamos Flash
# from celeryfuncion import make_celery
#
app = Flask(__name__) ##creamos una aplicacion Flask de esta forma con el consatrutor de l clase
# flask_app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379'
# )
# celery = make_celery(flask_app)

@app.get("/")#pagina principal
def principal(): # muestra este mensaje por pantalla
    return "<h1> hola, buenos dias mundo</h1>"

@app.get("/adios")
def adios():
    return "<h2> Adios manita querida </h2>"

@app.get("/saludar/<nombre>") #ruta dinamicas, ya que la ultima parte es variable
def saludar(nombre):
    return "<h1> Hola {} buenos dias </h2>".format(nombre)

@app.get("/longitud/<nombre>") #ruta dinamicas, ya que la ultima parte es variable
def longitud(nombre):
    valor = len(nombre)
    return "<h1> La palabra {} tiene {} letras </h2>".format(nombre, valor)

@app.get("/edad/<nombre>/<edad>") #ruta dinamicas, ya que la ultima parte es variable
def edad(nombre, edad):
    return "<h1> {} tiene {} años </h2>".format(nombre, edad)

@app.get("/sumar/<numero1>/<numero2>") #ruta dinamicas, ya que la ultima parte es variable
def suma(numero1, numero2):
    resultado = int(numero1) + int(numero2)
    suma = str(resultado)
    return "<h1> La suma de {} y {} es {} </h1>".format(numero1, numero2, resultado)


if __name__ == '__main__': # verifica que es el programa principal
    app.run(debug=True)
