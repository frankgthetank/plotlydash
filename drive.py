from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import json

# Configurar las credenciales de la cuenta de servicio
#SERVICE_ACCOUNT_FILE = r'/etc/secrets/poryectodedrive-97e74b45d2fb.json'
SERVICE_ACCOUNT_FILE = r'/etc/secrets/poryectodedrive-97e74b45d2fb.json'
#
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Crear servicio de Google Drive
service = build('drive', 'v3', credentials=creds)

# Descargar un archivo de Google Drive
def download_geojson(file_id, destination):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Descargando {int(status.progress() * 100)}%.")
    print("Archivo descargado correctamente.")
    #with open('temp/temp_geojson.geojson', 'r', encoding='utf-8') as f:
    #    return json.load(f)

# Usar la función para descargar el archivo
#file_id = '1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0'  # Reemplaza con tu file_id
#download_geojson(file_id, 'temp_geojson.geojson')
