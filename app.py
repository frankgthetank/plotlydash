import drive_api
import dash
from dash import dcc, html
import plotly.express as px
import drive
#import pandaframe
import pandas as pd
px.set_mapbox_access_token('pk.eyJ1IjoiZnJhbmpvZ29yZGlsbG8yNCIsImEiOiJjbTRsamlrOWIwMmo5MnFwbXd6eWpwNTQ1In0.r8O0UqVGKQtrYqogKBnIuA')
  
#geojson_data = drive_api.download_geojson_from_drive('1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0')
geojson_data = drive.download_geojson('1HkHBBb5chWjcua97xS-xqvx4OCX5Ijq0', 'temp_geojson.geojson')

# Leer el archivo GeoJSON
url = 'https://raw.githubusercontent.com/frankgthetank/plotlydash/refs/heads/main/midataarchivo1.csv'

df = pd.read_csv(url)

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Esto es necesario para que Gunicorn sepa cuál es el objeto llamable del servidor
server = app.server  # Esto hace que `server` esté disponible para Gunicorn
# Mostrar el contenido del GeoDataFrame








# Crear el mapa interactivo usando Plotly Express
fig = px.choropleth_mapbox(
    df,
    geojson=geojson_data,
    locations='nom_par',
    featureidkey='features.properties.nom_par',  # Clave del GeoJSON correspondiente
    #color='parroquia',
    mapbox_style="carto-positron",
    zoom=10,
    center={"lat": -0.22985, "lon": -78.52495},
    opacity=0.6,
    width=1500,  # Ancho del mapa
    height=600  # Altura del mapa
)



# Layout de la aplicación Dash
app.layout = html.Div([
    html.H1("Mapa interactivo con Plotly Dash y GeoJSON desde Google Drive", style={'text-align': 'center'}),
    
    # Componente Graph para visualizar el mapa
    dcc.Graph(figure=fig),
    
    # Aquí puedes agregar otros componentes como controles, sliders, etc.
])

"""

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)
print("llego al final sin problema")

"""

# Asegúrate de que la aplicación sea ejecutable
if __name__ == "__main__":
    app.run_server(debug=True)