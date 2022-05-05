'''
    Layout for Page 2 (Main page)
'''

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from styles import styles
from header import displayPathogen, displayInfoTable
from edge_info import displayNetworkGraph
from virus_node_info import display_v_node_properties
from mouse_node_info import display_m_node_properties
from footer import create_footer

'''
    Create navigation bar
'''
def create_navbar():
    navbar = html.Div([
        
        html.Div([
            html.H1("Online Analytic for Host-Pathogen Protein Interactions Analysis"),
        ], style=styles['nav-bar-header']),

        html.Div([
            dbc.NavbarBrand(
                dcc.Link(
                    dbc.Button(
                        children='HOME', 
                        style=styles['nav-bar-btn'] 
                    ),
                    href='/home'
                ),
            ),
        ], style=styles['nav-bar-btn-div']),

    ], style=styles['nav-bar'])

    return navbar

def create_main_content():
    return html.Div([
        
        create_navbar(),

        html.Div([

            html.Div([
                displayPathogen(),
                displayInfoTable(),
            ], id='header', style=styles['header']),

            html.Div([
                 
                html.Div([
                    displayNetworkGraph(),
                ], id='left-panel', style=styles['left-panel']),
                 
                html.Div([
                    html.Div([
                         html.H6('Click on a node to view properties', style=styles['default-para-head']),
                    ], style={'height':'30px'}),
                   
                    html.Div([
                        html.H5("Virus Nodes", style=styles['default-header']),
                        display_v_node_properties(), 
                    ], id='top-virus', style=styles['node-info']),

                    html.Div([
                        html.H5("Mouse Nodes", style=styles['default-header']),
                        display_m_node_properties(), 
                    ], id='btm-mouse', style=styles['node-info']),

                ], id='right-panel', style=styles['right-panel']),

            ], id='body', style=styles['body']),

            create_footer(),

        ], id='main-container', style=styles['main-container'])
        
        
    ], id='main-pg', style=styles['webpage'])