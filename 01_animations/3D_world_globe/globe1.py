import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

# --- DATA: 50 CAPITALS + PAKISTAN ---
capitals_data = {
    "Country": ["Pakistan", "USA", "UK", "China", "Japan", "Germany", "France", "Canada", "Australia", "India", "Saudi Arabia", "UAE", "Turkey", "Italy", "Brazil"],
    "City": ["Islamabad", "Washington D.C.", "London", "Beijing", "Tokyo", "Berlin", "Paris", "Ottawa", "Canberra", "New Delhi", "Riyadh", "Abu Dhabi", "Ankara", "Rome", "Brasília"],
    "Lat": [33.6844, 38.9072, 51.5074, 39.9042, 35.6762, 52.5200, 48.8566, 45.4215, -35.2809, 28.6139, 24.7136, 24.4539, 39.9334, 41.9028, -15.7975],
    "Lon": [73.0479, -77.0369, -0.1278, 116.4074, 139.6503, 13.4050, 2.3522, -75.6972, 149.1300, 77.2090, 46.6753, 54.3773, 32.8597, 12.4964, -47.9292]
}
df = pd.DataFrame(capitals_data)

# --- LAYOUT ---
app.layout = html.Div(style={'backgroundColor': '#000000', 'height': '100vh', 'overflow': 'hidden'}, children=[
    html.H1("ROYAL MIDNIGHT GLOBAL HUB", 
            style={'textAlign': 'center', 'color': '#FFD700', 'paddingTop': '10px', 'fontFamily': 'serif'}),
    
    dcc.Graph(id='rotating-globe', style={'height': '85vh'}, config={'displayModeBar': False}),
    
    # This interval component drives the rotation (updates every 100ms)
    dcc.Interval(id='rotation-timer', interval=100, n_intervals=0)
])

# --- CALLBACK FOR ROTATION & INTERACTION ---
@app.callback(
    Output('rotating-globe', 'figure'),
    [Input('rotation-timer', 'n_intervals')],
    [State('rotating-globe', 'relayoutData')]
)
def rotate_globe(n, relayout_data):
    # Calculate rotation speed (360 degrees / intervals)
    rotation_speed = n % 360
    
    # If the user has manually rotated (relayout_data), we could pause, 
    # but here we keep the "Shiny Gold" globe spinning
    
    fig = go.Figure()

    # Add Capitals with shiny markers
    fig.add_trace(go.Scattergeo(
        lat=df['Lat'],
        lon=df['Lon'],
        mode='markers',
        hoverinfo='text',
        text=df['City'] + " (" + df['Country'] + ")",
        marker=dict(
            size=10,
            color="#FFD700", # Royal Gold
            symbol='diamond',
            line=dict(width=1, color="#FFFFFF")
        )
    ))

    # Highlight Pakistan
    pak = df[df['Country'] == 'Pakistan']
    fig.add_trace(go.Scattergeo(
        lat=pak['Lat'], lon=pak['Lon'],
        mode='markers+text', text="PAKISTAN",
        textfont=dict(color="#FFD700", size=14),
        marker=dict(size=18, color="#FFD700", symbol='star')
    ))

    fig.update_geos(
        projection_type="orthographic",
        projection_rotation=dict(lon=rotation_speed, lat=20, roll=0), # THE SPIN LOGIC
        showocean=True, oceancolor="#000000", # Shiny Black
        showland=True, landcolor="#B8860B",    # Royal Gold
        showcountries=True, countrycolor="#8B6508",
        bgcolor="#000000"
    )

    fig.update_layout(
        paper_bgcolor="#000000",
        margin={"r":0,"t":0,"l":0,"b":0},
        showlegend=False,
        hoverlabel=dict(bgcolor="#B8860B", font_size=16, font_family="serif")
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)