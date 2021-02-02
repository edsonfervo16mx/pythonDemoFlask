#pip install flask
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo con flask!"

@app.route("/demo")
def demo():
    return "Demo con flask!"

#http://localhost:8000/saludo?name=juana&mensaje=bienvenido
@app.route("/saludo")
def saludo(name='Mundo',mensaje="saludos"):
    name =request.args.get("name",name)
    mensaje = request.args.get("mensaje", mensaje)
    return "Hola {}, {}!".format(name,mensaje)

#http://localhost:8000/notificacion/
#http://localhost:8000/notificacion/pamela
@app.route("/notificacion/")
@app.route("/notificacion/<name>")
def notificacion(name="Usuario"):
    name = request.args.get("name", name)
    return "{} es necesario que contacte al admin".format(name)

#http://localhost:8000/add/4.3/7.3
#http://localhost:8000/add/5.7/7
#http://localhost:8000/add/4/7
#http://localhost:8000/add/4/9.3
@app.route("/add/<float:num1>/<float:num2>")
@app.route("/add/<float:num1>/<int:num2>")
@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<int:num1>/<float:num2>")
def add(num1,num2):
    #return "{} + {} + {}".format(num1,num2,int(num1)+int(num2)) para -> @app.route("/add/<num1>/<num2>")
    return "{} + {} + {}".format(num1, num2, num1 + num2) #declarando el tipo desde la ruta <int:num1>/<int:num2>

#http://localhost:8000/demo/html
@app.route("/demo/html")
def demohtml():
    return """
    <!doctype html>
    <html>
        <head>
            <title>Demo Html</title>
        </head>
        <body>
            <h1>Bienvenido</h1>
            <p>Hola a python with flask</p>
        </body>
    </html>
    """

#http://localhost:8000/render/html/textoquequieres
@app.route("/render/html/<mensaje>")
def renderhtml(mensaje="Bienvenido a Flask con Python"):
    #mensaje = request.args.get("mensaje", mensaje)
    context = {"texto": mensaje}
    return render_template("layout.html",**context)

app.run(debug=True, port=8000, host='127.0.0.1')

