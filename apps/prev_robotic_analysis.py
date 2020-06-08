from datetime import datetime as dt
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import re
from app import app
from app import app
from dash.dependencies import Input, Output
import pandas as pd
from app import app
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd
from datetime import datetime
import numpy as np
import pandas as pd
import scipy
import plotly.express as px
colors = {
    'background': '#fbfbfb',
    'background2': '#fbfbfb',
    'text': 'black'
    }
df3 = pd.read_csv('./data/wi_robot_table.csv')
robot_df = pd.read_csv('./data/robot_waste_categories.csv')
waste_category = df3['waste_type'].unique()
robot_category = df3['robot_name'].unique()
#robot_category.sort()
waste_df = pd.read_csv('./data/waste_categories.csv')
robot_df = pd.read_csv('./data/robot_waste_categories.csv')
#waste_category = waste_df['waste_categories'].unique()
def dynamo(date1,date2,ob):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('wi_table')
    response = table.scan(
    #KeyConditionExpression=Attr('timestamp').between(20200506, 20200508),
    #Attr('timestamp').between('{0}'.format(date),'{0}'.format(date2))
    FilterExpression=Attr('timestamp').between('{0}'.format(date1),'{0}'.format(date2)) & Attr('robot').eq('{0}'.format(ob))
    )
    items = response['Items']
    da=pd.DataFrame(items)
    dq=da['object'].unique()
    print(items[0])
    timestamp = []
    for i in range(len(items)):

        x = items[i]
        x_ts = x.get('timestamp')
        x_ts = x_ts.split(' ')
        x_ts = x_ts[1]
        timestamp.append(x_ts)
    print(timestamp)
    timestamp_col = {
            'timestamp':timestamp
            }
    df = pd.DataFrame(timestamp)
    start_time = min(timestamp)
    end_time = max(timestamp)
    st_h = start_time.split(':')
    st_h = int(st_h[0])
    print(st_h)
    et_h = end_time.split(':')
    et_h = int(et_h[0])
    incrementer = 10
    timestamp_freq_name = []
    timestamp_freq_value = []
    for i in range(st_h,et_h +1):
        mins = 0
        for j in range(0,6):
            counter = 0
            for k in timestamp:
                h_m = k.split(':')
                h = int(h_m[0])
                m = int(h_m[1])
                if h == i:
                    if mins<=m<mins+incrementer:
                        counter+=1
            timestamp_freq_name.append('{0}:{1}-{2}'.format(i,mins,mins+ incrementer))
            timestamp_freq_value.append(counter)
            mins+=incrementer
    print(timestamp_freq_name)
    print(timestamp_freq_value)
    return timestamp_freq_name,timestamp_freq_value

#date = datetime.fromisoformat('2020-05-05T12:30:59.000000')
opts =[{'label': i, 'value': i} for i in robot_category]
layout = html.Div([
    html.H3('Select the Robot:'),
        dcc.Dropdown(
        id='select-type1',
        options=[{'label': i, 'value': i} for i in robot_category],
        value='R1',
        multi=False,
            style={"width": "70%",
                   'display': 'inline-block'}
    ),
                 #html.Div([
                                #html.Label(['Choose a range:'],style={'font-weight': 'bold'}),
              #dcc.RadioItems(
                #    id='radio',
                 #   options=[
                  #           {'label': 'Single Date', 'value': 'start_date'},
                   #          {'label': 'Multiple Dates ', 'value': 'end_date'},
                   #] )
    #]),
    html.H3('Select the Dates:'),
    html.Div(
      dcc.DatePickerRange(
                       id='date-input1',
                       stay_open_on_select=False,
                       min_date_allowed=df3['date_time'].min(),
                       max_date_allowed=df3['date_time'].max(),
                       initial_visible_month=dt.now(),
                       start_date=df3['date_time'].min(),
                       end_date=df3['date_time'].max(),
                       number_of_months_shown=1,
                       month_format='MMMM,YYYY',
                       display_format='YYYY-MM-DD',
                       style={
                              'color': '#fbfbfb',
                              'font-size': '20px',
                              'padding-bottom': '20px',
                       }
       ),
      
          
      
     style={'marginTop': 0, 'marginBottom': 0, 'font-size': 30, 'color': 'white'}),
      html.H3('Select the Date Range:'), 
      html.Div(
         dcc.RangeSlider(
                            id='rangeslider1',
                            min=0,
                            max=df3['date_time'].nunique()-1,
                            value=[0, df3['date_time'].nunique()-1],
                            allowCross=False,
                            updatemode="mouseup",
                            ),
                                                            
         ),
      html.Div(id='graph-output1'),
                      
    

                     ],  style={
                                 "height": "700px",
                                 "width":"1200px",   
                                "background": "#fbfbfb"}
              )  
              
#@app.callback(Output('date-input','start_date'),
 #             [Input('radio','value')])
#def update_start(r_value):
 #   return np.sort(df3['date_time'].unique())[r_value[0]]
#@app.callback(Output('date-input','end_date'),
 #             [Input('radio','value')])
#def update_end(r_value):
 #   return np.sort(df3['date_time'].unique())[r_value[1]]              
@app.callback(Output('date-input1','start_date'),
              [Input('rangeslider1','value')])
def update_daterangestart(rangeslider_value):
    return np.sort(df3['date_time'].unique())[rangeslider_value[0]]
@app.callback(Output('date-input1','end_date'),
              [Input('rangeslider1','value')])
def update_daterangeend(rangeslider_value):
    return np.sort(df3['date_time'].unique())[rangeslider_value[1]] 
@app.callback(Output('graph-output1', 'children'),
              [Input('date-input1', 'start_date'),
               Input('date-input1', 'end_date'),
               Input('select-type1','value')])
      
def render_graph(start_date, end_date,value):
    timestamp_freq_name,timestamp_freq_value = dynamo(start_date,end_date,value)
    print(start_date)
    print(end_date)
    print(value)
    return dcc.Graph(
    id='graph-1',
        figure={
            'data': [
                {'x': timestamp_freq_name, 'y': timestamp_freq_value, 'type': 'line', 'name': 'value'},
            ],
            'layout': {
                'title': 'Usage Graph',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text'],
                    'size': 18
                },
                'xaxis': {
                        'title': 'Time',
                        'showspikes': True,
                        'spikedash': 'dot',
                        'spikemode': 'across',
                        'spikesnap': 'cursor',
                        },
                'yaxis': {
                        'title': 'Robot Usage',
                        'showspikes': True,
                        'spikedash': 'dot',
                        'spikemode': 'across',
                        'spikesnap': 'cursor'
                        },

            }
        }
    )
                
