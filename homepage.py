import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from navbar import Navbar

nav = Navbar()


body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("London Commute Experience"),
                     html.P(html.Pre(
                         """\
                         This is a detailed multi page app 
                         aimed to provide key insights into
                         various attributes of London 
                         Transporation Network. 
                         We cover the following points:
                         1. Accident Data
                         """)),
                      html.Br(),
                      html.P("""1. Twitter Data"""),


                     html.Br(),

                     html.P(""" ABCD """),


                           dbc.Button("View details", color="secondary"),
                   ],
                  md=6,
               ),
              dbc.Col(
                 [
                     html.H2("Graph"),
                     dcc.Graph(
                         figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def Homepage():
    layout = html.Div([nav,body])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()