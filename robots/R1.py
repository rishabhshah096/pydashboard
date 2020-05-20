import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output
import pandas as pd
from app import app


layout = html.Div([
    html.Div( id='r1-content' ),
    dcc.RadioItems(
        id='r1-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),

    html.Br(),

])

@app.callback(Output('r1-content', 'children'),
              [Input( 'app-1-dropdown', 'value' )])
def r1_radios(value):
    return 'You have selected "{}"'.format(value)