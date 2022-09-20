## Page 1

# import dash_core_components as dcc
# import dash_html_components as html

from importlib.resources import path
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from homepage import create_home_page
from main_page import create_main_content
from maindash import app

server = app.server
# app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    # Component represents the location or address bar in web browser
    dcc.Location(id='url', pathname='/home'), # refresh=False
    html.Div(id='page-content'),
    
    dcc.Store(id='store-pathogen', storage_type='session'), ## Global variable: For passing to main content page ## !important define storage_type='session'
    dcc.Store(id='store-taxonomy', storage_type='session'),
    dcc.Store(id='store-v-node', storage_type='memory'), ## The memory store reverts to the default on every page refresh
    # dcc.Store(id='store-chosen-organ', storage_type='session') ## To allow reading from mouse_vital
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):

    if pathname == '/home':
        return create_home_page()
    elif pathname== '/main-content':
        return create_main_content()

    # if pathname == '/main-content':
    #     return create_main_content()
    # else:
    #     return create_home_page()

if __name__ == '__main__':
    app.run_server(debug=False)