import dash
import base64

from styles import styles
from dash import html
from dash import dcc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

from contact_page import create_contact_page
from home_page import create_icon

## Read image
image_filename = 'use_help_diagram.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

def create_help_page():

    return html.Div([

        ## Header: Navigation bar
        html.Div([

            ## Left: Placeholder Div
            html.Div(style=styles['nav-bar-L-sub-div']),

            ## Centre: Header
            html.Div([
                DashIconify(icon="healthicons:virus-research", width=60, height=60), 
                html.H1("Virulence Network for IAV-Mouse PPI Analysis"),
            ], id='home-page-header', style=styles['nav-bar-header-div']),

            ## Right: Button(s)
            html.Div([
                html.Div([
                    dbc.NavbarBrand( ## Call out attention to a brand name or site title within a navbar
                        dcc.Link(
                            dbc.Button(
                                children='Search', 
                                style=styles['nav-bar-btn']
                            ),
                            href='/search'
                        ),
                    ),
                ], style=styles['nav-bar-btn-div']),

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
                ],style=styles['nav-bar-btn-div']), 

            ], style=styles['nav-bar-R-sub-div']),

        ], style=styles['nav-bar']),

        ## Main Section
        html.Div([

            ### Left-Div
            html.Div([

                ## Section header
                html.Div([
                    html.H3("About", style=styles['default-header']),
                ], style=styles['hp-content-header-div']),
                
                ## Top
                html.Div([
                    html.P(
                    'In IAV-Mouse PPI web server, a comprehensive virulence network of predicted domain-domain interaction(s) (DDI) between ' + 
                    'Influenza A virus (IAV) and mouse host proteins was presented. ' +
                    'IAV-Mouse PPI web server built on a previously published dataset involving lethal dose studies of IAV infections in mice ' + 
                    'and took into account strain-specific virulence levels (i.e., median lethal dose (LD50)).' + 
                    '\n\n' + 
                    'SUPERFAMILY 2.0 sequence search was used to map regions of an amino acid sequence to at least one Structural Classification of Proteins (SCOP) domain(s) ' +
                    'using the SUPERFAMILY hidden Markov models. ' + 
                    'Then, Domain Interaction Statistical Potential (DISPOT) was applied to determine and score putative DDIs.' + 
                    '\n\n' + 
                    'Ultimately, IAV-Mouse PPI web server allows the systematic study of disease factors, aids IAV disease modeling and ' + 
                    'can possibly contribute to computational methods for uncovering IAV infection mechanisms ' + 
                    'mediated through protein domain interactions between viral and host proteins.'
                    ),
                ], style=styles['hp-LR-content-top-div']),

                ## Bottom
                html.Div([
                    html.P('Links', style={'font-weight' : 'bold'}),
                    
                    html.Div([
                        dcc.Link(
                            children = 'Previously published dataset by F.X. Ivan and C.K. Kwoh (Additional file 5: Table S1)',
                            href='https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6295-8#Sec20', 
                            target='https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6295-8#Sec20'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),
                
                    html.Div([
                        dcc.Link(
                            children = 'UniProt Knowledgebase(KB)/Proteomes database',
                            href='https://www.uniprot.org/', 
                            target='https://www.uniprot.org/'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),

                    html.Div([
                        dcc.Link(
                            children = 'SUPERFAMILY 2.0 database',
                            href='https://supfam.org/sequence/search', 
                            target='https://supfam.org/sequence/search'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),

                    html.Div([
                        dcc.Link(
                            children = 'DISPOT',
                            href='http://dispot.korkinlab.org/home/pairs', 
                            target='http://dispot.korkinlab.org/home/pairs'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),
                    
                    html.Div([
                        dcc.Link(
                            children = 'IAV-Mouse PPI web server source code',
                            href='https://github.com/tengann/IAV-Host-PPI-Database', 
                            target='https://github.com/tengann/IAV-Host-PPI-Database'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),

                    html.Div([
                        dcc.Link(
                            children = 'IAV-Mouse PPI web server manuscript (Preprint)',
                            href='https://www.biorxiv.org/content/10.1101/2022.10.11.511722v1', 
                            target='https://www.biorxiv.org/content/10.1101/2022.10.11.511722v1'
                        , style={'font-size' : '14px'}),
                    ], style={'margin-top':'5px'}),
                ], style=styles['hp-L-content-btm-div']),
            ], style=styles['hp-L-main-div']),

            ### Right-Div
            html.Div([

                html.Div([
                    html.H3("Instructions for use", style=styles['default-header']),
                ], style=styles['hp-content-header-div']),

                html.Div([
                    html.P(
                        'IAV-Mouse PPI web server includes various features, namely, browsing via IAV subtype and strain to view information collected from literature searches, ' + 
                        'an interactive network graph with accompanying information on node (IAV & mouse SCOP domain) and edge (interacting IAV-mouse domain pairs) attributes, ' + 
                        'as well as amino acid sequences extracted from UniProt Knowledgebase(KB)/Proteomes database.'  
                    ),
                ], style=styles['hp-LR-content-top-div']),
                
                ## Insert Flowchart
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())) ## Use .decode()
                ], style=styles['hp-R-content-btm-div']),

            ], style=styles['hp-R-main-div']),
        ]),

        ## Footer: Contacts Panel
        create_contact_page(),

    ], id='help-pg', style=styles['webpage'])