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
df1['vSCOP_ID'] = df1['vSCOP_ID'].astype(str)

# Viral Uniprot IDs Dataframe
iav_df = pd.read_csv("./excel/IAV_interacting.csv", na_filter = False)
iav_df['vFamilyID'] = iav_df['vFamilyID'].astype(str)

# Mouse Uniprot IDs + SCOP domains Dataframe
df_mp = pd.read_csv("./excel/mouse_protein_domains.csv")

def display_v_node_properties():
    return html.Div(id='v_node_properties-div', style=styles['node-table-div'])
    
@app.callback(
    [Output('v_node_properties-div', 'children'),
    Output('store-v-node', 'data')],
    [Input('interaction-overview', 'tapNode'),
    Input('interaction-overview', 'tapEdge'),
    Input('store-pathogen', 'data'),
    Input('store-taxonomy', 'data')] ## Retrieve from homepage
)

# Return Superfamily Node Properties
def displayVirusNodeData(node_data, edge_data, chosen_pathogen, chosen_tax_id):
    
    data = []
    v_node_props_df = pd.DataFrame() ## init empty dataframe
    properties_list = ['Segment', 'UniProt ID', 'SCOP Superfamily ID', 'Superfamily', 'SCOP Start/End Residue(s)']
    v_node_props_df['Properties'] = properties_list

    dfu_f = iav_df[iav_df['TaxonomyID']==chosen_tax_id] 
    
    ctx = dash.callback_context
    if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapNode'):
        
        if node_data['classes']=='vNodes':

            superfam_id = node_data['data']['label'].split(' ')[1]

        elif node_data['classes']=='mNodes':
            # print('exit')
            return ""

    elif (ctx.triggered[0]['prop_id'].split('.')[1]=='tapEdge'):
        superfam_id = edge_data['sourceData']['label'].split(' ')[1]
    
    superfam_id = superfam_id.replace('(','').replace(')','')
    
    ## Retrieve from dfu_f
    vSuperfamily_df = dfu_f[dfu_f['vFamilyID'] == superfam_id]
    get_uniprot_id = vSuperfamily_df['UniProt_ID'].values[0]
    get_superfam_name = vSuperfamily_df['vSuperfamily'].values[0]
    get_residue = vSuperfamily_df['vSCOP'].values[0]

    ## Retrieve segment in full from interaction_overview (df1)
    v_seg_df = df1[df1['vSCOP_ID'] == superfam_id]
    get_segment_name = v_seg_df['vSegment'].values[0]
    
    data.extend((get_segment_name,
                get_uniprot_id,
                superfam_id,
                get_superfam_name,
                get_residue))

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
        ),
        get_uniprot_id,
    )