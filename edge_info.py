'''
    Retrieve Edge Information
'''
from maindash import app
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash import dash_table

from dash.dependencies import Input, Output
from styles import styles

from network import cytoscape_graph

df1 = pd.read_csv("./excel/interaction_overview.csv")

def displayNetworkGraph():

    return html.Div([

        html.Div([
            cytoscape_graph(), 
        ], id='display-graph', style=styles['display-graph']),

        html.Div([
            html.H5("DISPOT Score", style=styles['default-header']),

            html.Div(id='edge-info', style=styles['edge-info']),

        ], id='wrapper', style=styles['edge-info-wrapper']),

    ], id='network-graph-div', style=styles['network-graph-div'])

@app.callback(
    Output('edge-info', 'children'),
    [Input('interaction-overview', 'tapEdge'),
    Input('interaction-overview', 'tapNode')]
)

def getInteractionScore(data, empty): 
    ctx = dash.callback_context

    if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapNode'): 
        return html.P('Click on an edge to view score', style=styles['default-para-head'])  

    elif (ctx.triggered[0]['prop_id'].split('.')[1]=='tapEdge'):
        data_arr = []
        edge_props_df = pd.DataFrame() 
        properties_list = ['Virus Node', 'Mouse Node', 'Score']
        edge_props_df['Properties'] = properties_list

        source_df=df1.loc[df1['vFamilyID']==data['sourceData']['label']]
        target_df=source_df.loc[source_df['mFamilyID']==data['targetData']['label']]

        v_node = target_df.vSuperfamily.unique() + ' ' + str(target_df.vSCOP_ID.unique())
        m_node = target_df.mSuperfamily.unique() + ' ' + str(target_df.mFamilyID.unique())
        score = target_df['score'].to_string(index=False)
    
        data_arr.extend((v_node, m_node, score))

        edge_props_df['Values'] = data_arr

        return (
            dash_table.DataTable(
                data=edge_props_df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in edge_props_df.columns],
                style_cell={'textAlign': 'left'},
                style_header={'display': 'none'},
                style_data=styles['style-data'],
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Properties'},
                        'backgroundColor' : '#97B3D0',
                        'font-weight' : 'bold'
                    },

                    {
                        'if': {'column_id': 'Values'},
                        'backgroundColor' : '#323232',
                        'color' : 'white'
                    },

                    {
                        'if' : {'state':'selected'},
                        'backgroundColor' : 'inherit !important',
                        'border' : 'inherit !important'
                    },
                ],
                fill_width=False,
            )
    )

    else: 
        return html.P('Click on an edge to view score', style=styles['default-para-head'])  