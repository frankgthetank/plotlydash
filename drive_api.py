

import os
import io
import json
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Configura el alcance y las credenciales
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CLIENT_SECRET_FILE = r'/etc/secrets/client_secret_1082915945888-sq1jradiqj5b7lbjf0nmnjo9ufv4gjtf.apps.googleusercontent.com.json'
#CLIENT_SECRET_FILE = r'C:\Users\anali\OneDrive\Documentos\PYTHON\PLOTLYDASH\client_secret_1082915945888-sq1jradiqj5b7lbjf0nmnjo9ufv4gjtf.apps.googleusercontent.com.json'

TOKEN_FILE = 'token.json'

def authenticate_google_account():
    """Autenticar con Google y crear un cliente para interactuar con la API de Drive"""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)            
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    
    service = build('drive', 'v3', credentials=creds)
    return service


def download_geojson_from_drive(file_id):
    """Descargar un archivo GeoJSON desde Google Drive."""
    service = authenticate_google_account()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO('temp/temp_geojson.geojson', 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Descargando {int(status.progress() * 100)}%.")
    print("Descarga completa.")
    with open('temp/temp_geojson.geojson', 'r', encoding='utf-8') as f:
        return json.load(f)


"""
def download_geojson_from_drive(service, file_id):
    #Descargar un archivo GeoJSON desde Google Drive
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO('temp_geojson.geojson', 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Descargando {int(status.progress() * 100)}%.")
    print("Descarga completa.")
    
    # Leer el archivo descargado y cargarlo como GeoJSON
    with open('temp_geojson.geojson', 'r',encoding='utf-8') as f:
        geojson_data = json.load(f)
    
    return geojson_data

# Llamada para autenticar y descargar el archivo
try:
    service = authenticate_google_account()
    file_id = '1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0'  # Reemplaza con el ID de tu archivo
    geojson_data = download_geojson_from_drive(service, file_id)
    print("GeoJSON descargado correctamente.")
except Exception as e:
    print(f"Error durante la autenticación o la descarga: {e}")
"""
    
