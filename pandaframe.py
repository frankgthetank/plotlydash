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

# Verificar las columnas disponibles
#print("Columnas disponibles en el GeoJSON:", df.columns)

# Obtener valores únicos de dos columnas
columna1 = "parroquia"  # Cambia por el nombre de la columna deseada
columna2 = "nom_par"  # Cambia por el nombre de la columna deseada

valores_unicos_columna1 = df[columna1].unique()
valores_unicos_columna2 = df[columna2].unique()


# Crear el nuevo DataFrame
df_resumido = pd.DataFrame({
    "codparrauni": pd.Series(valores_unicos_columna1), # Aseguramos que las series tengan igual longitud
    "nomparrauni": valores_unicos_columna2  
})

gdf = gpd.GeoDataFrame(df_resumido, geometry='geometry')

# Guardar el DataFrame en un archivo GeoJSON
gdf.to_file("data.geojson", driver='GeoJSON')

print("DataFrame guardado en 'data.geojson'.")

#columnas_seleccionadas = ["valores_unicos_columna1", "valores_unicos_columna2"]
#df_resumido = df[columnas_seleccionadas]

#print(f"Valores únicos en '{columna1}':", valores_unicos_columna1)
#print(f"Valores únicos en '{columna2}':", valores_unicos_columna2)
#print(df_resumido.head())