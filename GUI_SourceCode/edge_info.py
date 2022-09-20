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

# from network import cytoscape_graph
from network import network_div

df1 = pd.read_csv("./excel/interaction_overview.csv")

def displayNetworkGraph():

    return html.Div([
        # html.H3("Network graph", style = {'font-family' : 'Verdana, sans-serif'}), ## Placeholder

        network_div(), ## html.Div

        ## In network-graph-div
        html.Div([
            html.H5("DISPOT Score", style=styles['default-header']),

            html.Div([
                html.P('Click on an edge to view score', style=styles['default-para-head']), ## Placeholder text
            ],id='edge-info', style=styles['edge-info']),

        ], id='wrapper', style=styles['edge-info-wrapper']),

    ], id='network-graph-div', style=styles['network-graph-div'])

@app.callback(
    Output('edge-info', 'children'),
    [Input('interaction-overview', 'tapEdge'),
    Input('interaction-overview', 'tapNode')]
)

def getInteractionScore(data, empty): # Takes 2 positional arguments (inputs)
    ctx = dash.callback_context

    # if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapNode'): ## Clear edge-info box if tap Node
    #     return html.P('Click on an edge to view score', style=styles['default-para-head'])  ## Placeholder Text

    if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapEdge'):
        data_arr = []
        edge_props_df = pd.DataFrame() ## init empty dataframe
        properties_list = ['Virus Node', 'Mouse Node', 'Score']
        edge_props_df['Properties'] = properties_list

        ## Get target domain
        source_df=df1.loc[df1['vFamilyID']==data['sourceData']['label']]
        target_df=source_df.loc[source_df['mFamilyID']==data['targetData']['label']]
        # dfu_f = dfu[dfu.Pathogen==chosen_pathogen]

        v_node = target_df.vSuperfamily.unique() + ' ' + str(target_df.vSCOP_ID.unique())
        m_node = target_df.mSuperfamily.unique() + ' ' + str(target_df.mFamilyID.unique())
        score = target_df['score'].to_string(index=False)
    
        data_arr.extend((v_node, m_node, score))

        edge_props_df['Values'] = data_arr
        # v_node_props_df.loc[len(v_node_props_df)] = data  ## Append as row


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
                        # 'color' : 'black',
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

    else: ## Nothing triggered 
        return html.P('Click on an edge to view score', style=styles['default-para-head'])  ## Placeholder Text