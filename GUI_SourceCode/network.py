'''
    Creates cytoscape graph
'''
from maindash import app
from styles import styles

import pandas as pd
import dash_cytoscape as cyto

from dash import html
from dash.dependencies import Input, Output

int_overview = pd.read_csv("./excel/interaction_overview.csv")
iav_df = pd.read_csv("./excel/IAV_interacting.csv")

## Filter taxonomy in IAV_interacting.csv
## If vSCOP_ID (interaction_overview.csv) isin vSCOP (IAV_interacting) -- plot graph
## new_df[new_df.vSCOP_ID.isin(f_int.vSCOP)].reset_index(drop=True)

def network_div():
    return html.Div(id='network-div', style=styles['display-graph'])

@app.callback(
    Output('network-div','children'),
    Input('store-taxonomy', 'data') ## Get Taxonomy ID
)

def cytoscape_graph(chosen_taxonomy):

    ## Filter taxonomy in IAV_interacting.csv
    iav_int_df = iav_df[iav_df['TaxonomyID']==chosen_taxonomy]

    ## If vSCOP_ID (interaction_overview.csv) isin vSCOP (IAV_interacting) -- plot graph
    df1  = int_overview[int_overview.vSCOP_ID.isin(iav_int_df.vFamilyID)].reset_index(drop=True)

    # Node Elements
    default_nodes = (
        [{'classes': 'vNodes', 
        'data':{'id': v, 'label': v}} for v in df1.vFamilyID.unique()]+
        [{'classes': 'mNodes',
        'data': {'id': m, 'label': m}} for m in df1.mFamilyID.unique()]
    )
    # Edge Elements
    default_edges = [{'classes': 'int_edges', 
    'data': {'source': x, 'target': y, 'weight':w}} for x,y,w in zip(df1.vFamilyID,df1.mFamilyID, df1.weight)]
     
    default_elements=(default_nodes+default_edges)

    default_stylesheet=[
    # Class Selectors
        {
            'selector':'.vNodes',
            'style': {
                'background-color': '#CA8EB0',
                'label': 'data(label)',
                'width': 40,
                'height': 40
            },
        },

        {
            'selector':'.mNodes',
            'style': {
                'background-color': '#5EB5C9',
                'label': 'data(label)',
                'width': 40,
                'height': 40
            },
        },

        {
            'selector':'.int_edges',
            'style': {
                'width': 'data(weight)'
            },
        }
    ]

    return cyto.Cytoscape(
        id='interaction-overview',
        layout={'name':'cose'},
        elements=default_elements,
        stylesheet=default_stylesheet,
        userPanningEnabled=False, #Lock graph in place
        userZoomingEnabled=False,
    )