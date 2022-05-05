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
df_mp_organ = pd.read_csv("./excel/mouse_vital.csv")

def display_m_node_properties():
    return html.Div([
        html.Div([
            html.Div([
                html.Label("SCOP Superfamily ID: ", style=styles['label']),
                dcc.Dropdown(
                    id = 'chosen-domain',
                    options=[{'label': i, 'value':i} for i in sorted (df1.mFamilyID.unique())],
                    disabled=True,
                    placeholder='Click Mouse Node',
                    style=styles['dropdown']
                ),
            ], style={
                'float':'left',
                'width': '60%'}),

            html.Div([
                html.Label("Filter by Organ:", style=styles['label']),
                dcc.Dropdown(
                    id = 'chosen-organ',
                    options = {},
                    clearable=True,
                    style=styles['organ-dropdown']
                ),
            ], style={
                'float': 'right',
                'width': '39%',
                'margin-left' : '0.5%'}),

        ], style={'display': 'flex'}),
        

        html.Div([
            html.Div([
                html.Label("Browse Proteins: ", style=styles['label']),
                dcc.Dropdown(
                    id = 'chosen-protein',
                    options = {},
                    clearable=False,
                    placeholder='Select SCOP Domain',
                    style=styles['dropdown']
                ),
            ], style={'float':'left',
                    'width': '60%'}),
        
            html.Div(style={'float':'right',
                            'width' : '40%'}),

        ], style={'margin-top': '10px',
                    'display':'flex',
                    'flex-direction' : 'column'}),
        
        html.Div(id='m_node_table', style=styles['node-table-div']),

    ], id='m_node_properties-div')
  
@app.callback(
    Output('chosen-domain', 'value'), 
    [Input('interaction-overview', 'tapNodeData'),
    Input('interaction-overview', 'tapEdge')]
)
def getDomain(node_data,edge_data):
    ctx = dash.callback_context
    if (ctx.triggered[0]['prop_id'].split('.')[1]=='tapNodeData'):
        return node_data['label']

    elif (ctx.triggered[0]['prop_id'].split('.')[1]=='tapEdge'):
        return edge_data['targetData']['label']

@app.callback(
    Output('m_node_table', 'children'),
    [Input('chosen-protein', 'value'),
    Input('chosen-domain', 'value'),
    Input('store-chosen-organ', 'data')]
)
def displayMouseNodeData(chosen_protein, chosen_domain, chosen_organ):
    if chosen_protein:
        m_data_arr = []
        m_node_props_df = pd.DataFrame() 
        properties_list = ['Protein', 'UniProt ID', 'SCOP Superfamily ID', 'Superfamily', 'SCOP Start/End Residue(s)']
        m_node_props_df['Properties'] = properties_list

        if chosen_organ is not None:
            filter_organ = df_mp_organ[df_mp_organ['Organ']==chosen_organ] 
            mSuperfamily_df=filter_organ[filter_organ['Protein']==chosen_protein] 

        else:
            mSuperfamily_df=df_mp.loc[df_mp['Protein']==chosen_protein] 
        
        mSuperfamily_df = mSuperfamily_df[mSuperfamily_df['mFamilyID']==chosen_domain]

        if len(mSuperfamily_df) > 1: 
            m_uniProt_ID = mSuperfamily_df['UniprotID'].values[0] 
        else:
            m_uniProt_ID = mSuperfamily_df['UniprotID'].values

        m_data_arr.extend((mSuperfamily_df.Protein.unique(),
                    m_uniProt_ID,
                    str(mSuperfamily_df.mFamilyID.unique()),
                    mSuperfamily_df.mSuperfamily.unique(), 
                    mSuperfamily_df['mSCOP'].to_string(index=False)))

        m_node_props_df['Values'] = m_data_arr

        return (
            dash_table.DataTable(
                data=m_node_props_df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in m_node_props_df.columns],
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

@app.callback(
    [Output('chosen-protein', 'options'),
    Output('chosen-organ', 'options'),
    Output('store-chosen-organ', 'data')],
    [Input('chosen-domain', 'value'),
    Input('chosen-organ', 'value')]
)
def filterMProteinOpts(chosen_domain, chosen_organ):
    org_organ_df = df_mp_organ[df_mp_organ.mFamilyID==chosen_domain] 
    organ_df = org_organ_df['Organ']
    organ_df = organ_df.drop_duplicates()
    organ_df = organ_df.reset_index(drop=True)
    organ_opts= [{'label':o, 'value':o} for o in sorted(organ_df.astype(str))]

    if chosen_organ is not None:
        get_protein = org_organ_df[org_organ_df.Organ==chosen_organ] 
        protein_opts=[{'label':mp, 'value':mp} for mp in sorted(get_protein.Protein.unique())]

    else:
        protein_df=df_mp[df_mp.mFamilyID==chosen_domain]
        protein_opts=[{'label':mp, 'value':mp} for mp in sorted(protein_df.Protein.unique())]

    return protein_opts, organ_opts, chosen_organ

@app.callback(
    Output('chosen-protein', 'value'), 
    Input('chosen-protein', 'options')
)
def callback(value):
    return ""