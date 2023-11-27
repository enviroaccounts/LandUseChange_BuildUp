from dash import Dash, html, dcc
import pandas as pd
import plotly.graph_objects as go

def load_builtup_area_data():
    """Loads land use change data for built-up areas."""
    return pd.read_csv("static/data/LandUseChange_BuildUp_1990_2016.csv")

def prepare_builtup_area_chart_data(data_df):
    """Prepares data for the built-up area land use pie chart."""
    # Extracting data from 'Forest' column onwards
    builtup_area_data = data_df.iloc[0, 3:]
    labels = builtup_area_data.index.tolist()
    values = builtup_area_data.values.tolist()
    return labels, values

def create_builtup_area_pie_chart(labels, values):
    """Creates a pie chart for built-up area land use data."""
    return go.Figure(data=[go.Pie(labels=labels, values=values)])

def setup_builtup_area_layout(app, fig_pie_chart):
    """Sets up the layout of the Dash app for built-up area visualization."""
    app.layout = html.Div(children=[
        html.Div([
            dcc.Graph(id='builtup-area-pie-chart', figure=fig_pie_chart)
        ]),
        html.Div([  
            html.H3(id='builtup-area-pie-chart-description', children='What was all this urbanised land before 1990?')
        ])
    ], id='builtup-area-pie-chart-layout')

def create_app():
    """Creates and configures the Dash app for built-up area data."""
    app = Dash(__name__)

    # Load and prepare data
    data_df = load_builtup_area_data()
    labels, values = prepare_builtup_area_chart_data(data_df)

    # Create pie chart
    fig_pie_chart = create_builtup_area_pie_chart(labels, values)

    # Setup layout
    setup_builtup_area_layout(app, fig_pie_chart)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run_server(debug=True, host='0.0.0.0', port=8050)
