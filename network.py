'''
    Creates cytoscape graph
'''

import pandas as pd
import dash_cytoscape as cyto

df1 = pd.read_csv("./excel/interaction_overview.csv")

def cytoscape_graph():
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