import json
import pandas as pd
import geopandas as gpd

# Cargar el archivo GeoJSON
geojson_file = r"C:\Users\anali\OneDrive\Documentos\output_filesectores.geojson"
with open(geojson_file, 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Extraer las propiedades de cada Feature
features = geojson_data.get("features", [])
data = [feature["properties"] for feature in features]

# Crear un DataFrame con las propiedades
df = pd.DataFrame(data)

# Obtener valores únicos de dos columnas
columna1 = "parroquia"  # Cambia por el nombre de la columna deseada
columna2 = "nom_par"  # Cambia por el nombre de la columna deseada

valores_unicos_columna1 = df[columna1].unique()
valores_unicos_columna2 = df[columna2].unique()

# Asegurar que ambas columnas tengan la misma longitud (rellenando si es necesario)
longitud_maxima = max(len(valores_unicos_columna1), len(valores_unicos_columna2))

# Rellenar con "Desconocido" si las longitudes no coinciden
valores_unicos_columna1 = list(valores_unicos_columna1) + ["Desconocido"] * (longitud_maxima - len(valores_unicos_columna1))
valores_unicos_columna2 = list(valores_unicos_columna2) + ["Desconocido"] * (longitud_maxima - len(valores_unicos_columna2))

# Crear el nuevo DataFrame con las columnas alineadas
df_resumido = pd.DataFrame({
    "parroquia": valores_unicos_columna1,
    "nom_par": valores_unicos_columna2
})

# Ver el DataFrame resultante


#print(df_resumido.head())




# Guardar el DataFrame en un archivo CSV en la ubicación deseada
df_resumido.to_csv('midataarchivo1.csv', index=False)

print("Archivo CSV guardado correctamente.")


#gdf = gpd.GeoDataFrame(df_resumido, geometry='geometry')

# Guardar el DataFrame en un archivo GeoJSON
#gdf.to_file("midata.geojson", driver='GeoJSON')

#print("DataFrame guardado en 'data.geojson'.")

#columnas_seleccionadas = ["valores_unicos_columna1", "valores_unicos_columna2"]
#df_resumido = df[columnas_seleccionadas]

#print(f"Valores únicos en '{columna1}':", valores_unicos_columna1)
#print(f"Valores únicos en '{columna2}':", valores_unicos_columna2)
#print(df_resumido.head())

