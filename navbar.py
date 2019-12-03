import dash_bootstrap_components as dbc
import dash_html_components as html

FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#4c4c57",
    "color": "#f4f5f7",
    #"color" : "dark",
    #"dark" : "True"
    "font-family" : "Arial"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


submenu_1 = [
    html.Li(
        # use Row and Col components to position the chevrons
        dbc.Row(    #Screen is split in rows and columns. This is the first row with 2 columns
            [

                dbc.Col("Twitter"),
                dbc.Col(
                    html.I(className="fas fa-chevron-down mr-3"), width="auto" #-down was -right. mr-X, X is the position
                ),

            ],
            className="my-1",
        ),
        id="submenu-1",
    ),
    # we use the Collapse component to hide and reveal the navigation links
    dbc.Collapse(
        [
            dbc.NavLink("Sentiment Analysis", href="/apps/t_sentiment"),
            dbc.NavLink("Word Cloud", href="/apps/t_cloud"),

        ],

        id="submenu-1-collapse",
    ),
]

submenu_2 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Accidents"),
                dbc.Col(
                    html.I(className="fas fa-chevron-down mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        id="submenu-2",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Borough Report", href="/apps/a_borough"),
            dbc.NavLink("Accident Locations", href="/apps/a_accidentmap"),
        ],
        id="submenu-2-collapse",
    ),
]

submenu_3 = [
    html.Li(
        dbc.Row(
            [
                dbc.Col("Usage Statistics"),
                dbc.Col(
                    html.I(className="fas fa-chevron-down mr-3"), width="auto"
                ),
            ],
            className="my-1",
        ),
        id="submenu-3",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Parking Infrastructure", href="/apps/a_park"),
            dbc.NavLink("Tube Usage", href="/apps/a_stationusage"),

        ],
        id="submenu-3-collapse",
    ),
]
def Navbar():
    navbar = html.Div(
        [
            html.Img(src='/assets/n9hyiWD.png',
            style={
                        'height' : '20%',
                        'width' : '100%',
                        #'float' : 'left',
                        'border-radius': '50%',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0
                    }
                     )
                    ,
            #html.H2("Sidebar", className="display-4"),
            html.Hr(), #This is a horizontal line
            html.P(
                "", className="lead"
            ),  #This is a paragraph
            dbc.Nav(submenu_1 + submenu_2 + submenu_3, vertical=True),
        ],
        style=SIDEBAR_STYLE,
        id="sidebar",
        #color = "dark",
        #dark = True
    )
    return navbar



'''

def Navbar():
     navbar = dbc.Nav(
           children=[
              #dbc.NavItem(dbc.NavLink("Twitter Sentiment Analysis", href="/time-series")),
               html.A(
                   # Use row and col to control vertical alignment of logo / brand
                   dbc.Row(
                       [
                           dbc.Col(html.Img(src='https://imgur.com/cLQBCvo.png', height="Auto",width = "150px")),
                           #dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                       ],
                       align="center",
                       no_gutters=True,
                   ),
                   href="/home",
               ),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Twitter",
                 children=[
                    #dbc.DropdownMenuItem("Sentiment Analysis"),
                    dbc.NavItem(dbc.NavLink("Sentiment Analysis", href="/t_sentiment")),
                    dbc.NavItem(dbc.NavLink("Word Cloud", href="/t_wordcloud")),
                    #dbc.DropdownMenuItem("Word Cloud"),
                    #dbc.DropdownMenuItem(divider=True),
                    #dbc.DropdownMenuItem("Entry 3"),
                          ],
                      ),
               dbc.DropdownMenu(
                   nav=True,
                   in_navbar=True,
                   label="Accident",
                   children=[
                       # dbc.DropdownMenuItem("Sentiment Analysis"),
                       dbc.NavItem(dbc.NavLink("Borough Report", href="/a_borough")),
                       #dbc.NavItem(dbc.NavLink("Word Cloud", href="/t_wordcloud")),
                       # dbc.DropdownMenuItem("Word Cloud"),
                       # dbc.DropdownMenuItem(divider=True),
                       # dbc.DropdownMenuItem("Entry 3"),
                   ],
               ),
                    ],
          #brand="Home",
          #brand_href="/home",
          #sticky="top",
         #vertical=True
        )
     #return sidebar
     return navbar

'''