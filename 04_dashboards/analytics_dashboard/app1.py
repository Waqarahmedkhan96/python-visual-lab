import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- THEME CONFIG ---
BG_COLOR = "#000000"
CYAN = "#00E5FF"
MAGENTA = "#FF007F"
LIME = "#32CD32"
TEXT_GRAY = "#A0A0A0"

app = dash.Dash(__name__)

def get_mock_data(size=40):
    x = np.linspace(0, 10, size)
    return pd.DataFrame({
        'x': x,
        'val1': 50 * np.exp(-x/3) + np.random.normal(0, 2, size),
        'val2': 20 + 30 * (1 - np.exp(-x/4)) + np.random.normal(0, 1, size)
    })

# --- LAYOUT ---
app.layout = html.Div(style={'backgroundColor': BG_COLOR, 'padding': '20px', 'minHeight': '100vh'}, children=[
    
    # Title Header
    html.H2("USERS: LAST 7 DAYS USING MEDIAN ⌵", 
            style={'color': 'white', 'fontSize': '18px', 'fontFamily': 'sans-serif', 'marginBottom': '20px'}),

    # 2x2 MAIN GRID
    html.Div(style={
        'display': 'grid', 
        'gridTemplateColumns': '1fr 1fr', 
        'gridTemplateRows': '1fr 1fr', 
        'gap': '30px', 
        'height': '85vh'
    }, children=[
        
        # Quadrant 1: Load Time vs Bounce
        html.Div([
            html.P("LOAD TIME VS BOUNCE RATE    ⚙ OPTIONS", style={'color': TEXT_GRAY, 'fontSize': '10px'}),
            dcc.Graph(id='q1', style={'height': '100%'}, config={'displayModeBar': False})
        ], style={'display': 'flex', 'flexDirection': 'column'}),

        # Quadrant 2: Start Render vs Bounce
        html.Div([
            html.P("START RENDER VS BOUNCE RATE    ⚙ OPTIONS", style={'color': TEXT_GRAY, 'fontSize': '10px'}),
            dcc.Graph(id='q2', style={'height': '100%'}, config={'displayModeBar': False})
        ], style={'display': 'flex', 'flexDirection': 'column'}),

        # Quadrant 3: Page Views vs Onload
        html.Div([
            html.P("PAGE VIEWS VS ONLOAD    ⚙ OPTIONS", style={'color': TEXT_GRAY, 'fontSize': '10px'}),
            dcc.Graph(id='q3', style={'height': '100%'}, config={'displayModeBar': False})
        ], style={'display': 'flex', 'flexDirection': 'column'}),

        # Quadrant 4: Sessions
        html.Div([
            html.P("SESSIONS    ⚙ OPTIONS", style={'color': TEXT_GRAY, 'fontSize': '10px'}),
            dcc.Graph(id='q4', style={'height': '100%'}, config={'displayModeBar': False})
        ], style={'display': 'flex', 'flexDirection': 'column'}),
    ])
])

# --- CALLBACK TO RENDER ALL 4 GRAPHS ---
@app.callback(
    [Output('q1', 'figure'), Output('q2', 'figure'), Output('q3', 'figure'), Output('q4', 'figure')],
    [Input('q1', 'id')]
)
def update_all_charts(_):
    df = get_mock_data()
    
    def create_fig(color1, color2, chart_type="mix"):
        fig = go.Figure()
        if chart_type == "mix":
            fig.add_trace(go.Bar(x=df['x'], y=df['val1'], marker_color=color1, opacity=0.7))
            fig.add_trace(go.Scatter(x=df['x'], y=df['val2'], line=dict(color=color2, width=2), yaxis="y2"))
        else:
            fig.add_trace(go.Scatter(x=df['x'], y=df['val1'], line=dict(color=color1, width=2)))
            fig.add_trace(go.Scatter(x=df['x'], y=df['val2'], line=dict(color=color2, width=2)))

        fig.update_layout(
            template="plotly_dark", paper_bgcolor=BG_COLOR, plot_bgcolor=BG_COLOR,
            margin=dict(l=10, r=10, t=10, b=30), showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, color="#444", tickfont=dict(size=8)),
            yaxis=dict(showgrid=False, visible=False),
            yaxis2=dict(overlaying='y', side='right', visible=False)
        )
        return fig

    # Returning 4 different variations to match the 4 quadrants
    return (
        create_fig(CYAN, MAGENTA, "mix"),    # Top Left
        create_fig(CYAN, MAGENTA, "mix"),    # Top Right
        create_fig(MAGENTA, CYAN, "lines"),  # Bottom Left
        create_fig(LIME, CYAN, "lines")      # Bottom Right
    )

if __name__ == '__main__':
    app.run(debug=True)