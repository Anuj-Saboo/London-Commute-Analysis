import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
#from app import App, build_graph
from app import app
#from Borough import borough
from apps import twitter,Borough,park,stationusage,accidentmap, twittercloud
from homepage import Homepage


def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""


for i in [1, 2,3]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

    app.callback(
        Output(f"submenu-{i}", "className"),
        [Input(f"submenu-{i}-collapse", "is_open")],
    )(set_navitem_class)

CONTENT_STYLE = {
    "font-family" : "Georgia"
}
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content',style=CONTENT_STYLE)
])
app.config['suppress_callback_exceptions']=True

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/t_sentiment':
        return twitter.layout
    elif pathname == '/apps/t_cloud':
        #return twittercloud.layout
        return Homepage()
    elif pathname == '/apps/a_borough':
        return Borough.layout
    elif pathname =='/apps/a_park':
        return park.layout
    elif pathname =='/apps/a_stationusage':
        return stationusage.layout
    elif pathname =='/apps/a_accidentmap':
        return accidentmap.layout

    elif pathname == '/home':
        return Homepage()
    else:
        return Homepage()

if __name__ == '__main__':
    app.run_server(debug=True)