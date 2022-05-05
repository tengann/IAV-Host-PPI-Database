'''
    Retrieve Node Information
'''
from email import header
from maindash import app
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash import dash_table

from dash.dependencies import Input, Output
from styles import styles

# Read interaction dataframe - overview
df1 = pd.read_csv("./excel/interaction_overview.csv")

# Viral Uniprot IDs Dataframe
dfu = pd.read_csv("./excel/viral_uniprot.csv")

# Mouse Uniprot IDs + SCOP domains Dataframe
df_mp = pd.read_csv("./excel/mouse_protein_domains.csv")

def display_v_node_properties():
    return html.Div(id='v_node_properties-div', style=styles['node-table-div'])
    
@app.callback(
    [Output('v_node_properties-div', 'children'),
    Output('store-v-node', 'data')],
    [Input('interaction-overview', 'tapNode'),
    Input('interaction-overview', 'tapEdge'),
    Input('store-pathogen', 'data')] 
)

def displayVirusNodeData(node_data, edge_data, chosen_pathogen):
    data = []
    v_node_props_df = pd.DataFrame() 
    properties_list = ['Segment', 'UniProt ID', 'SCOP Superfamily ID', 'Superfamily', 'SCOP Start/End Residue(s)']
    v_node_props_df['Properties'] = properties_list

    dfu_f = dfu[dfu.Pathogen==chosen_pathogen] 

    ctx = dash.callback_context
    if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapNode'):
        if node_data['classes']=='vNodes':
            vSuperfamily_df=df1[df1.vFamilyID==node_data['data']['label']]
            get_uniprot_id = dfu_f[node_data['data']['label']].to_string(index=False) 
        elif node_data['classes']=='mNodes':
            return ""

    elif (ctx.triggered[0]['prop_id'].split('.')[1]=='tapEdge'):
        vSuperfamily_df=df1[df1.vFamilyID==edge_data['sourceData']['label']]
        get_uniprot_id = dfu_f[edge_data['sourceData']['label']].to_string(index=False)

    data.extend((vSuperfamily_df.vSegment.unique(),
                get_uniprot_id,
                str(vSuperfamily_df.vSCOP_ID.unique()),
                vSuperfamily_df.vSuperfamily.unique(),
                vSuperfamily_df.vSCOP.unique()))

    v_node_props_df['Values'] = data

    return (
        dash_table.DataTable(
            data=v_node_props_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in v_node_props_df.columns],
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
        ),
        get_uniprot_id,
    )