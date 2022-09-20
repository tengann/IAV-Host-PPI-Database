'''
    Layout for Page 1 (aka Homepage)
'''

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from styles import styles
from dropdown_func import dropdown_func

## Homepage

def create_home_page():
    return html.Div([
        
        ## Header
        html.Div([
            html.H1("Online Analytic for Host-Pathogen Protein Interactions Analysis"),
        ], id='home-page-header', style=styles['home-page-header']),

        ## Align at center 
        html.Div([
            
            dropdown_func(), ## html.Div

            ## Search Button
            html.Div([
                dcc.Link(
                    dbc.Button(
                        children='SEARCH', 
                        style=styles['nav-bar-btn'] ## default size
                    ),
                    href='/main-content',
                    # refresh=True
                ),
            ], style={'margin-top':'20px'}),

        ], style=styles['home-page-container']),
        
    ], id='home-pg', style=styles['webpage'])