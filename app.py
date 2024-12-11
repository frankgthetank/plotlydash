import drive_api
import dash
from dash import dcc, html
import plotly.express as px
import drive
#import pandaframe
import pandas as gpd

#geojson_data = drive_api.download_geojson_from_drive('1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0')
geojson_data = drive.download_geojson('1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0', 'temp_geojson.geojson')
# Crear la aplicación Dash
app = dash.Dash(__name__)
server = app.server

# Leer el archivo GeoJSON
url = 'https://raw.githubusercontent.com/frankgthetank/plotlydash/refs/heads/main/midataarchivo.csv'

gdf = gpd.read_csv(url)




# Mostrar el contenido del GeoDataFrame


# Crear el mapa interactivo usando Plotly Express
fig = px.choropleth_mapbox(
    gdf,
    geojson=geojson_data,
    locations='codparrauni',  # Cambiar según los datos del GeoJSON
    color='nomparrauni',   # Cambiar según los datos del GeoJSON
    mapbox_style="carto-positron",
    zoom=10,
    center={"lat": 0, "lon": 0},
)

# Layout de la aplicación Dash
app.layout = html.Div([
    html.H1("Mapa interactivo con Plotly Dash y GeoJSON desde Google Drive", style={'text-align': 'center'}),
    
    # Componente Graph para visualizar el mapa
    dcc.Graph(figure=fig),
    
    # Aquí puedes agregar otros componentes como controles, sliders, etc.
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)
print("llego al final sin problema")



