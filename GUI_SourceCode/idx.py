## Page 1
# from importlib.resources import path

# import dash_core_components as dcc
# import dash_html_components as html

# import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from home_page import create_home_page
from main_page import create_main_content
from about_help_page import create_help_page
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

    if pathname == '/home': ## page to display
        return create_home_page()
    elif pathname == '/help':
        return create_help_page()
    elif pathname== '/search':
        return create_main_content()

if __name__ == '__main__':
    app.run_server(debug=False)