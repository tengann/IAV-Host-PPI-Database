'''
    Layout for Page 1 (Home page)
'''

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from styles import styles
from dropdown_func import dropdown_func

def create_home_page():
    return html.Div([
        
        html.Div([
            html.H1("Online Analytic for Host-Pathogen Protein Interactions Analysis"),
        ], id='home-page-header', style=styles['home-page-header']),

        html.Div([
            
            dropdown_func(), 

            html.Div([
                dcc.Link(
                    dbc.Button(
                        children='SEARCH', 
                        style=styles['nav-bar-btn'] 
                    ),
                    href='/main-content',
                ),
            ], style={'margin-top':'20px'}),

        ], style=styles['home-page-container']),
        
    ], id='home-pg', style=styles['webpage'])