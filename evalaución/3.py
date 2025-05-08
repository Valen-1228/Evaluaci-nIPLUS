
import requests
from requests.auth import HTTPBasicAuth

host = "https://hga09pj16jk.sn.mynetname.net"
endpoint = "/rest/ppp/secret"
url = host + endpoint

usuario = "1Prueb@USr"
contraseña = "Ap1P@ssw0rd.1S3gurO"

nuevo_usuario = {
    "name": "Valen", 
    "password": "claveSegura123", 
    "service": "pppoe",
    "profile": "Home-120Mbps",
    "remote-address": "192.168.121.15",
    "comment": "AlexanderValentinGordilloRojas"
}

response = requests.put(url, json=nuevo_usuario, auth=HTTPBasicAuth(usuario, contraseña), verify=False)

if response.status_code in [200, 201]:
    print("Registro creado correctamente en /rest/ppp/secret.")
    print("Respuesta del router:")
    print(response.text)
else:
    print(f"Error al crear el registro: {response.status_code}")
    print(response.text)
