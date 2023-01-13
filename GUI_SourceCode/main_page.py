'''
    Layout for Page 2
'''

from dash import html
from dash import dcc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

from styles import styles
from header import displayPathogen, displayInfoTable
from edge_info import displayNetworkGraph
from virus_node_info import display_v_node_properties
from mouse_node_info import display_m_node_properties
from footer import create_footer

from contact_page import create_contact_page

'''
    Create navigation bar
'''
def create_main_content():
    
    return html.Div([
        
        ## Navigation bar
        html.Div([

            ## Left: Placeholder Div
            html.Div(style=styles['nav-bar-L-sub-div']),

            ## Centre: Header
            html.Div([
                DashIconify(icon="healthicons:virus-research", width=60, height=60), 
                html.H1("Online Analytic for IAV-Mouse PPI Analysis"),
            ], id='home-page-header', style=styles['nav-bar-header-div']),

            ## Right: Button(s)
            html.Div([

                ## Home Button
                html.Div([
                    dbc.NavbarBrand( ## Call out attention to a brand name or site title within a navbar
                        dcc.Link(
                            dbc.Button(
                                children='Home', 
                                style=styles['nav-bar-btn']
                            ),
                            href='/home'
                        ),
                    ),
                ], style=styles['nav-bar-btn-div']),
                
                ## Help Button
                html.Div([
                    dbc.NavbarBrand( 
                        dcc.Link(
                            dbc.Button(
                                children='Help', 
                                style=styles['nav-bar-btn']
                            ),
                            href='/help'
                        ),
                    ),
                ],style=styles['nav-bar-btn-div']), 

            ], style=styles['nav-bar-R-sub-div']),

        ], style=styles['nav-bar']),

        ## main-container
        html.Div([

            html.Div([
                displayPathogen(),
                displayInfoTable(),
            ], id='header', style=styles['header']),

            html.Div([
                
                #  html.H6("Body"),
                 
                html.Div([

                    # html.H6("Left"), ## Placeholder
                    displayNetworkGraph(),
                    # get_protein_seq(),

                ], id='left-panel', style=styles['left-panel']),
                 
                html.Div([

                    # html.H6("Right"), ## Placeholder
                    html.Div([
                         html.H6('Click on a node to view properties', style=styles['default-para-head']),
                    ], style={'height':'30px'}),
                   
                    # html.P('Click on a node to view properties'), ## Placeholder paragraph
                    
                    ## display_node_info(),
                    html.Div([
                        html.H5("Virus Nodes", style=styles['default-header']),
                        display_v_node_properties(), ## returns div (virus node properties) table
                    ], id='top-virus', style=styles['node-info']),

                    html.Div([
                        html.H5("Mouse Nodes", style=styles['default-header']),
                        display_m_node_properties(), # returns 1 div (w/ sub-divs, for 3 dropdowns and 1 table)
                    ], id='btm-mouse', style=styles['node-info']),

                ], id='right-panel', style=styles['right-panel']),

            ], id='body', style=styles['body']),

            create_footer(),

            # html.Div([
            #     html.H6("Footer"),


            # ], id='footer', style=styles['footer']),

        ], id='main-container', style=styles['main-container']),

        ## Contacts Panel
        create_contact_page(),
        
        
    ], id='main-pg', style=styles['webpage'])