import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from apps import today_robotic_analysis, today_waste_analysis,prev_waste_analysis
from robots import R1

'''
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

'''

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Home", href="/home", id="page-1-link"),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Dashboard", header=True),
                        dbc.DropdownMenuItem("Today", href="/apps/today_waste_analysis",id="page-2-link"),
                        dbc.DropdownMenuItem("Previous", href="/apps/prev_waste_analysis",id = "page-3-link"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Waste analytics",
                ),

                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Dashboard", header=True),
                        dbc.DropdownMenuItem("Today", href="/apps/today_robotic_analysis",id="page-4-link"),
                        dbc.DropdownMenuItem("Previous", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Robot-analytics",
                ),
            ],
            brand="Wastefull Insights",
            brand_href="#",
            color="primary",
            dark=True,
        ),
        dbc.Container(id="page-content", className="pt-4"),
    ]
)
path_list = ['/apps/today_waste_analysis','/apps/prev_waste_analysis','/robots/R1','/apps/today_robotic_analysis']
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 5)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False,False
    print(pathname)
    print([pathname == f"{i}" for i in path_list])
    return [pathname == f"{i}" for i in path_list]


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname in ["/", "/home"]:
        home_string = 'Welcome to wastefull-insights, this is the best platform to recieve detailed analysis and ' \
                      'live streaming of the waste which is being segregated'
        return html.P("{0}".format(home_string))
    if pathname == '/apps/today_waste_analysis':
        return today_waste_analysis.layout
    if pathname == '/apps/prev_waste_analysis':
        return prev_waste_analysis.layout
    if pathname == '/robots/R1':
        return R1.layout
    elif pathname == '/apps/today_robotic_analysis':
        return today_robotic_analysis.layout

    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)