import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
import pandas as pd
from app import app

waste_df = pd.read_csv('./data/waste_categories.csv')
robot_df = pd.read_csv('./data/robot_waste_categories.csv')
waste_category = waste_df['waste_categories'].unique()

def card_maker(robot_number):
    return dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4( "{0}".format(str(robot_number)), className="card-title" ),
                            html.P(
                                "Speed = 3.1 ",
                                className="card-text",
                            ),
                            dbc.CardLink( "{0}-Analytics".format(str(robot_number)), href="/robots/R1" ),

                        ]
                    ),
                    style={"width": "18rem"},
                    id="robot_card-" + str(robot_number)
                    )

layout = html.Div([
    html.H3('Robot-Analysis'),
        html.Br(style={
                'line-height': 100
                }),
    html.P('Select the Waste Category'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[{'label': i, 'value': i} for i in waste_category],
        value = 'ALL'
    ),
    html.Hr(),
    html.Div(
        id = 'cards',
        className="cards",
        style={'padding-left':'0px','padding-right':'150px', 'maxHeight': '650px', 'line-height':40,}
        )
])


@app.callback(
    Output('cards', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    if value == 'ALL':
        working_robots = robot_df.loc[1:,:]
        return [card_maker(robot_number) for robot_number in working_robots]
    else:
        working_robots = (robot_df.columns[robot_df.isin( ['{0}'.format( value )] ).any()])
        return [card_maker(robot_number) for robot_number in working_robots]
