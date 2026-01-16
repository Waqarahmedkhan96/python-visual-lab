import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- BEST THEME CONFIG ---
BG_COLOR = "#000000"     # Pure Black background
CYAN = "#00ADB5"         # Neon Cyan for bars
MAGENTA = "#FF2E63"      # Neon Magenta for lines
TEXT_COLOR = "#EEEEEE"

app = dash.Dash(__name__)

# Mock Data Generation
def get_data():
    x = np.linspace(0, 20, 50)
    return pd.DataFrame({
        'time': x,
        'load_time': np.exp(-x/5) * 60 + np.random.normal(0, 2, 50),
        'bounce_rate': 40 + 20 * np.sin(x/4) + np.random.normal(0, 1, 50)
    })

df = get_data()

# Layout Structure
app.layout = html.Div(style={'backgroundColor': BG_COLOR, 'padding': '20px'}, children=[
    html.H2("USERS: LAST 7 DAYS USING MEDIAN", style={'color': TEXT_COLOR, 'fontFamily': 'Arial'}),
    
    # KPI Row
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '20px'}, children=[
        html.Div([html.P("Page Load (LUX)", style={'color': CYAN}), html.H3("0.7s", style={'color': TEXT_COLOR})]),
        html.Div([html.P("Page Views (LUX)", style={'color': MAGENTA}), html.H3("2.7Mpvs", style={'color': TEXT_COLOR})]),
        html.Div([html.P("Bounce Rate (LUX)", style={'color': MAGENTA}), html.H3("40.6%", style={'color': TEXT_COLOR})]),
        html.Div([html.P("Sessions (LUX)", style={'color': CYAN}), html.H3("479K", style={'color': TEXT_COLOR})])
    ]),

    # Main Graph Grid
    html.Div(style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'}, children=[
        # Quadrant 1: Load Time vs Bounce
        dcc.Graph(
            figure=go.Figure()
            .add_trace(go.Bar(x=df['time'], y=df['load_time'], marker_color=CYAN, name="Load Time"))
            .add_trace(go.Scatter(x=df['time'], y=df['bounce_rate'], line=dict(color=MAGENTA, width=2), name="Bounce Rate"))
            .update_layout(
                title="LOAD TIME VS BOUNCE RATE",
                plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR,
                font_color=TEXT_COLOR, showlegend=False,
                margin=dict(l=40, r=40, t=40, b=40)
            )
        ),
        
        # Quadrant 2: Start Render vs Bounce
        dcc.Graph(
            figure=go.Figure()
            .add_trace(go.Bar(x=df['time'], y=df['load_time'][::-1], marker_color=CYAN))
            .add_trace(go.Scatter(x=df['time'], y=df['bounce_rate'][::-1], line=dict(color=MAGENTA, width=2)))
            .update_layout(
                title="START RENDER VS BOUNCE RATE",
                plot_bgcolor=BG_COLOR, paper_bgcolor=BG_COLOR,
                font_color=TEXT_COLOR, showlegend=False
            )
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)