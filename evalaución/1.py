import requests
from requests.auth import HTTPBasicAuth

host = "https://hga09pj16jk.sn.mynetname.net"
endpoint = "/rest/user"
url = host + endpoint

usuario = "1Prueb@USr"
contraseña = "Ap1P@ssw0rd.1S3gurO"

response = requests.get(url, auth=HTTPBasicAuth(usuario, contraseña), verify=False)

print(f"Status Code: {response.status_code}")
print("Contenido:")
print(response.json())
