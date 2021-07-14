from flask import Flask ,  render_template

app = Flask(__name__)

@app.get("/")
def portada():
    return render_template("portada.html")

@app.get("/hola")
def hola():
    valor = "Libia"
    valor_edad = 43
    diccionario = {'nombre':'Libia', 'edad':'43', 'color':'azul'}
    return render_template("hola.html", datos = diccionario )

@app.get("/colores")
def colores():
    lista_colores = ["verde", "amarillo", "azul", "rojo", "naranja", "rosado"]
    return render_template("colores.html", colores = lista_colores)

@app.get("/frase/<texto>")
def frase(texto):
    return render_template("frase.html", tipo=texto)


if __name__ == '__main__': # verifica que es el programa principal
    app.run(debug=True)
