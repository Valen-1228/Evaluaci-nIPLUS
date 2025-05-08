import requests
from requests.auth import HTTPBasicAuth

host = "https://hga09pj16jk.sn.mynetname.net"
endpoint = "/rest/ppp/secret"
url = host + endpoint

usuario = "1Prueb@USr"
contraseña = "Ap1P@ssw0rd.1S3gurO"

try:
    response = requests.get(url, auth=HTTPBasicAuth(usuario, contraseña), verify=False)

    if response.status_code == 200:
        print("Conexión exitosa. Datos obtenidos del endpoint /rest/ppp/secret:\n")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.json()}")
except Exception as e:
    print(f"Excepción al conectar: {e}")
