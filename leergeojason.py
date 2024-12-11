import json

# Ruta al archivo GeoJSON
geojson_file = r"C:\Users\anali\OneDrive\Documentos\output_filesectores.geojson"



# Leer el archivo GeoJSON
with open(geojson_file, 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Inspeccionar las claves principales del archivo
print("Claves principales del archivo GeoJSON:", geojson_data.keys())

# Leer las primeras características (features) del GeoJSON
if 'features' in geojson_data:
    print("Primer registro (Feature):")
    print(json.dumps(geojson_data['features'][0], indent=2))  # Muestra la primera "Feature" con formato
else:
    print("No hay 'features' en el archivo GeoJSON.")
