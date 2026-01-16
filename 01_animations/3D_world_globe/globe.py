import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

# --- DATA: 50 CAPITALS + PAKISTAN ---
capitals_data = {
    "Country": ["Pakistan", "USA", "UK", "China", "Japan", "Germany", "France", "Canada", "Australia", "India", 
                "Brazil", "Russia", "Saudi Arabia", "UAE", "Turkey", "Italy", "Spain", "Mexico", "South Africa", "Egypt",
                "Norway", "Sweden", "Netherlands", "Switzerland", "Argentina", "Chile", "Nigeria", "Kenya", "Thailand", "Singapore",
                "South Korea", "Vietnam", "Indonesia", "Malaysia", "New Zealand", "Greece", "Portugal", "Austria", "Belgium", "Denmark",
                "Finland", "Ireland", "Poland", "Czech Republic", "Hungary", "Ukraine", "Iran", "Iraq", "Qatar", "Kuwait", "Egypt"],
    "City": ["Islamabad", "Washington D.C.", "London", "Beijing", "Tokyo", "Berlin", "Paris", "Ottawa", "Canberra", "New Delhi",
             "Brasília", "Moscow", "Riyadh", "Abu Dhabi", "Ankara", "Rome", "Madrid", "Mexico City", "Pretoria", "Cairo",
             "Oslo", "Stockholm", "Amsterdam", "Bern", "Buenos Aires", "Santiago", "Abuja", "Nairobi", "Bangkok", "Singapore",
             "Seoul", "Hanoi", "Jakarta", "Kuala Lumpur", "Wellington", "Athens", "Lisbon", "Vienna", "Brussels", "Copenhagen",
             "Helsinki", "Dublin", "Warsaw", "Prague", "Budapest", "Kyiv", "Tehran", "Baghdad", "Doha", "Kuwait City", "Cairo"],
    "Lat": [33.6844, 38.9072, 51.5074, 39.9042, 35.6762, 52.5200, 48.8566, 45.4215, -35.2809, 28.6139,
            -15.7975, 55.7558, 24.7136, 24.4539, 39.9334, 41.9028, 40.4168, 19.4326, -25.7479, 30.0444,
            59.9139, 59.3293, 52.3676, 46.9480, -34.6037, -33.4489, 9.0765, -1.2921, 13.7563, 1.3521,
            37.5665, 21.0285, -6.2088, 3.1390, -41.2865, 37.9838, 38.7223, 48.2082, 50.8503, 55.6761,
            60.1699, 53.3498, 52.2297, 50.0755, 47.4979, 50.4501, 35.6892, 33.3152, 25.2854, 29.3759, 30.0444],
    "Lon": [73.0479, -77.0369, -0.1278, 116.4074, 139.6503, 13.4050, 2.3522, -75.6972, 149.1300, 77.2090,
            -47.9292, 37.6173, 46.6753, 54.3773, 32.8597, 12.4964, -3.7038, -99.1332, 28.2293, 31.2357,
            10.7522, 18.0686, 4.9041, 7.4474, -58.3816, -70.6693, 7.3986, 36.8219, 100.5018, 103.8198,
            126.9780, 105.8542, 106.8456, 101.6869, 174.7762, 23.7275, -9.1393, 16.3738, 4.4674, 12.5683,
            24.9384, -6.2603, 21.0122, 14.4378, 19.0402, 30.5234, 51.3890, 44.3661, 51.5310, 47.9774, 31.2357]
}

df = pd.DataFrame(capitals_data)

# --- CREATE THE SHINY GOLD & BLACK GLOBE ---
fig = go.Figure()

# Add Capitals as "Shiny" points
fig.add_trace(go.Scattergeo(
    lat=df['Lat'],
    lon=df['Lon'],
    mode='markers',
    hoverinfo='text',
    text=df['City'] + " (" + df['Country'] + ")",
    marker=dict(
        size=8,
        color="#FFD700", # Gold markers
        symbol='diamond',
        line=dict(width=1, color="#FFFACD") # Shiny outer glow
    )
))

# Highlight Pakistan specifically
pak_df = df[df['Country'] == 'Pakistan']
fig.add_trace(go.Scattergeo(
    lat=pak_df['Lat'],
    lon=pak_df['Lon'],
    mode='markers+text',
    text="PAKISTAN",
    textposition="top center",
    marker=dict(size=15, color="#FFD700", symbol='star')
))

fig.update_geos(
    projection_type="orthographic",
    showocean=True, oceancolor="#000000", # Deep Black Ocean
    showland=True, landcolor="#B8860B",    # Dark Gold Land
    showcountries=True, countrycolor="#8B6508", # Shiny borders
    showlakes=False,
    bgcolor="#000000"
)

fig.update_layout(
    paper_bgcolor="#000000",
    plot_bgcolor="#000000",
    height=800,
    margin={"r":0,"t":0,"l":0,"b":0},
    showlegend=False
)

app.layout = html.Div(style={'backgroundColor': '#000000', 'height': '100vh'}, children=[
    html.H1("ROYAL GOLD GLOBAL CAPITALS", 
            style={'textAlign': 'center', 'color': '#FFD700', 'paddingTop': '20px', 'fontFamily': 'serif'}),
    dcc.Graph(figure=fig, style={'height': '85vh'})
])

if __name__ == '__main__':
    app.run(debug=True)