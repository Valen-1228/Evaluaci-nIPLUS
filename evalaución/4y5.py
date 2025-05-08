import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template, request

host = "https://hga09pj16jk.sn.mynetname.net"
endpoint = "/rest/ppp/secret"
url = host + endpoint

usuario = "1Prueb@USr"
contraseña = "Ap1P@ssw0rd.1S3gurO"

app = Flask(__name__)

@app.route("/")
def inicio():
    responsee = requests.get(url, auth=HTTPBasicAuth(usuario, contraseña), verify=False)
    response = responsee.json()
    return render_template("index.html", posts=response)

@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre", "")
    responsee = requests.get(url, auth=HTTPBasicAuth(usuario, contraseña), verify=False)
    response = responsee.json()

    resultados = [d for d in response if nombre.lower() in d["name"].lower()]
    return render_template("index.html", posts=resultados)

if __name__ == "__main__":
    app.run(debug=True)
