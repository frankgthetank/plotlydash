
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
df_resumido.to_csv('midataarchivo2.csv', index=False)

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







"""

import json
import pandas as pd

# Cargar el archivo GeoJSON
geojson_file = "C:\\Users\\anali\\OneDrive\\Documentos\\output_filesectores.geojson"
with open(geojson_file, 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Extraer las propiedades de cada Feature
features = geojson_data.get("features", [])
data = [feature.get("properties", {}) for feature in features]

# Crear un DataFrame con las propiedades
df = pd.DataFrame(data)

# Rellenar valores faltantes
# Rellenar columnas no numéricas con "Desconocido"
columnas_no_numericas = df.select_dtypes(exclude=["number"]).columns
df[columnas_no_numericas] = df[columnas_no_numericas].fillna("Desconocido")

# Rellenar columnas numéricas con un valor específico, como 0
columnas_numericas = df.select_dtypes(include=["number"]).columns
df[columnas_numericas] = df[columnas_numericas].fillna(0)

# Obtener valores únicos de las columnas deseadas
columna1 = "parroquia"  # Cambia por el nombre de la columna deseada
columna2 = "nom_par"  # Cambia por el nombre de la columna deseada

# Validar que las columnas existan en el DataFrame
if columna1 in df.columns and columna2 in df.columns:
    valores_unicos_columna1 = df[columna1].drop_duplicates().tolist()
    valores_unicos_columna2 = df[columna2].drop_duplicates().tolist()

    # Asegurar que ambas columnas tengan la misma longitud
    longitud_maxima = max(len(valores_unicos_columna1), len(valores_unicos_columna2))
    valores_unicos_columna1 += ["Desconocido"] * (longitud_maxima - len(valores_unicos_columna1))
    valores_unicos_columna2 += ["Desconocido"] * (longitud_maxima - len(valores_unicos_columna2))

    # Crear el nuevo DataFrame con las columnas alineadas
    df_resumido = pd.DataFrame({
        "parroquia": valores_unicos_columna1,
        "nom_par": valores_unicos_columna2
    })

    # Guardar el DataFrame en un archivo CSV
    output_csv = 'midataarchivo4.csv'
    df_resumido.to_csv(output_csv, index=False)
    print(f"Archivo CSV guardado correctamente en: {output_csv}")

else:
    print(f"Las columnas '{columna1}' y/o '{columna2}' no existen en el archivo GeoJSON.")

"""