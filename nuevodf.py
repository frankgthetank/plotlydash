import json
import pandas as pd

# Ruta del archivo GeoJSON
geojson_file = r"C:\Users\anali\OneDrive\Documentos\output_filesectores.geojson"

# Cargar el archivo GeoJSON
with open(geojson_file, 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Extraer las propiedades de las Features
features = geojson_data.get("features", [])
data = [feature["properties"] for feature in features]

# Crear un DataFrame con las propiedades
df = pd.DataFrame(data)

# Definir las columnas que deseas extraer
columna1 = "parroquia"  # Cambia por el nombre de la columna que deseas
columna2 = "nom_par"    # Cambia por el nombre de la columna que deseas

# Seleccionar solo las dos columnas que necesitas
df_seleccionado = df[[columna1, columna2]]

# Eliminar duplicados asegurando que las filas se mantengan correspondientes
df_sin_duplicados = df_seleccionado.drop_duplicates()

# Mostrar el DataFrame resultante
print(df_sin_duplicados)

# Guardar el DataFrame en un archivo CSV
df_sin_duplicados.to_csv('output_dataframe_sin_duplicados.csv', index=False)
print("Archivo CSV guardado correctamente.")
