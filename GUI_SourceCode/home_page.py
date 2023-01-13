'''
    Layout for Page 1 (aka Homepage)
'''
from styles import styles

import dash
from dash import html
from dash import dcc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

from dropdown_func import dropdown_func
from contact_page import create_contact_page

## Homepage

def create_icon():
    return html.Div([

        DashIconify(icon="healthicons:virus-research",
                    width=250,
                    height=250)

    ], style=styles['icon-container'])
    
def create_home_page():
    return html.Div([
        
        ## Navigation bar
        html.Div([

            ## Left: Placeholder Div
            html.Div(style=styles['nav-bar-L-sub-div']),

            ## Centre: Header
            html.Div([
                # DashIconify(icon="healthicons:virus-research", width=60, height=60, color='#323232'), ## Placeholder, Camouflage icon
                html.H1("Online Analytic for IAV-Mouse PPI Analysis"),
            ], id='home-page-header', style=styles['nav-bar-header-div']), 

            ## Right: Button(s)
            html.Div([
                html.Div([
                    dbc.NavbarBrand( ## Call out attention to a brand name or site title within a navbar
                        dcc.Link(
                            dbc.Button(
                                children='Help', 
                                style=styles['nav-bar-btn']
                            ),
                            href='/help'
                        ),
                    ),
                ], style=styles['nav-bar-btn-div']),

                html.Div(style=styles['nav-bar-btn-div']), ## Placeholder

            ], style=styles['nav-bar-R-sub-div']),

        ], style=styles['nav-bar']),

        ## Align at center 
        html.Div([

            ## Icon
            create_icon(),
            
            dropdown_func(), ## html.Div

            ## Search Button
            html.Div([
                dcc.Link(
                    dbc.Button(
                        children='Search', 
                        style=styles['nav-bar-btn'] ## default size
                    ),
                    href='/search',
                    # refresh=True
                ),
            ], style={'margin-top':'20px'}),

            ## Content Summary
            html.Div([
                html.P('57 journal publications\n 14 IAV subtypes, 109 IAV strains, 2419 mouse proteins', style=styles['home-txt']), ## 'para-txt'
            ], style={'margin-top':'20px', 'text-align': 'center'})


        ], style=styles['home-page-container']),

        create_contact_page(), ## html.Div
        
    ], id='home-pg', style=styles['webpage'])