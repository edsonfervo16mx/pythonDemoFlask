from flask import Flask
from flask import request

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

app.run(debug=True, port=8000, host='127.0.0.1')

