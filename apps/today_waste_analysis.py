import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash
from app import app
from dash.dependencies import Input, Output
import pandas as pd
from app import app
import plotly.express as px
df3 = pd.read_csv('./data/wi_robot_table.csv')
robot_df = pd.read_csv('./data/robot_waste_categories.csv')
waste_category = df3['waste_type'].unique()
waste_category.sort()
df = pd.read_csv('./data/waste_categories.csv')
robot_df = pd.read_csv('./data/robot_waste_categories.csv')
#waste_category = df['waste_categories'].unique()
layout = html.Div([
    html.H6('Live Data'),
        html.Div(
         dcc.Graph(id='waste1', figure={})
             ),     
    html.P('Select the Waste Category'),
    dcc.Dropdown(
        id='appdropdown',
        options=[{'label': i, 'value': i} for i in waste_category],
        value = 'waste_type'
    ),
            dcc.Graph(id='waste', figure={}),
            
       html.P('Select the Waste Category'),
    dcc.Dropdown(
        id='appdropdown1',
        options=[{'label': i, 'value': i} for i in df3.waste_type],
        value = 'waste_type'
    ),
            dcc.Graph(id='waste11', figure={}),
    #dcc.Link('Go to Page 1', href='/home'),
    #html.Br(),
    #dcc.Link('Go back to home', href='/')
])
@app.callback(
    Output(component_id='waste1', component_property='figure'),
    [Input(component_id='appdropdown', component_property='value')])
def update_graph(appdropdown):
    dff = df3

    piechart=px.pie(
            data_frame=dff,
            names=appdropdown,
            )

    return (piechart)

@app.callback(
    Output(component_id='waste11', component_property='figure'),
    [Input(component_id='appdropdown1', component_property='value')]
)

def update_graph1(appdropdown1):
    dff = df3

    bargraph=px.bar(
            data_frame=dff,
            x=df3,
            y=df3['date_time']
            )

    return (bargraph)


if __name__ == '__main__':
    app.run_server(debug=True)
#@app.callback(
    #Output('page-2-content', 'children'),
    #[Input('app-1-dropdown', 'value')])
#def page_2_dropdown(value):
    #return 'You have selected "{}"'.format(value)
