from ftplib import FTP

# Datos de conexión
host = '45.70.13.134'
usuario = 'usuario'
contraseña = 'ftp123'

# Conectar al servidor FTP
ftp = FTP(host)
ftp.login(user=usuario, passwd=contraseña)

# Archivo remoto y local
archivo_remoto = 'Evaluacion de Software.docx'
archivo_local = 'Evaluacion_de_Software_descargado.docx'

# Descargar
with open(archivo_local, 'wb') as f:
    ftp.retrbinary(f'RETR {archivo_remoto}', f.write)

print(f"Archivo descargado: {archivo_local}")

# Subir archivo
archivo_subir = 'Evaluacion_de_Software_Valentin_Gordillo.pdf'
with open(archivo_subir, 'rb') as f:
    ftp.storbinary(f'STOR {archivo_subir}', f)

ftp.quit()
