from maindash import app
import pandas as pd
import dash
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, State
from styles import styles

from bs4 import BeautifulSoup
import requests

## IAV dataframes
v_uni = pd.read_csv("./excel/viral_uniprot.csv", na_filter = False)
all_domains = pd.read_csv("./excel/IAV_all_domains.csv", na_filter = False)
interact_df = pd.read_csv("./excel/IAV_interacting.csv", na_filter = False)

# Mouse Uniprot IDs + SCOP domains Dataframe
df_mp = pd.read_csv("./excel/mouse_protein_domains.csv")

'''
    Insert Buttons
'''
def create_footer():
    return html.Div([

        # html.H6("Footer"),

        html.Div([
            html.Div([
                html.Button("Protein Sequence", id='protein-seq-btn', style=styles['btn']),
            ]),

            html.Div([
                html.Button("Non-interacting Viral Segments", id='no-int-btn', style=styles['btn']),
            ], style={'margin-left':'5px'}),

            html.Div([
                html.Button("Abbreviations", id='abbrv-btn', style=styles['btn']),
            ], style={'margin-left':'5px'}),

        ], id='footer-btn-container', style=styles['footer-sub-div']),

        ## Sub-header 
        html.Div(id='footer-sub-header', style=styles['footer-sub-head-div']),
       
        html.Div(id='footer-div-content', style=styles['footer-sub-div']),

    ], id='footer', style=styles['footer'])

## Non-interacting/Uniprot ID NOT FOUND viral protein domains
def write_no_int():

    no_int_content = (
        html.Div([
            html.Div(id='no-int-info-div'),
            html.P('\nFor Segment(s) where UniProt ID was "Not Found", Superfamily cannot be retrieved due to missing protein sequence information.\n Therefore it was not possible to predict any domain interaction.' , style=styles['para-txt']),
        ])
    )
    
    return no_int_content

## Protein Sequence
def write_protein_seq():
    ## Return to footer-div-content
    protein_seq_content = (

        html.Div([
            html.Div([
                html.H6("Virus", style=styles['default-header']),
            ], id='v-seq-header', style=styles['seq-header-div']),

            html.Div(id='v-seq-div', style=styles['seq-sub-div']),
            
        ], style=styles['seq-div']),

        html.Div([
            html.Div([
                html.H6("Mouse", style=styles['default-header']),
            ],id='m-seq-header', style=styles['seq-header-div']),

            html.Div(id='m-seq-div', style=styles['seq-sub-div']),

        ], style=styles['seq-div'])
    )

    return protein_seq_content
    
def write_abbv():
    
    abbv_content =  (

        # html.H5("Abbreviations", style=styles['default-header']),

        html.Div([
            html.P(' LD50 - Lethal Dose 50 ', style=styles['default-para-head']),
            html.P(" LD50 was used as the indicator of each pathogen's acute toxicity.\n " + 
                    "It refers to the dose required to kill half the members of a tested population after a specified test duration. \n" + 
                    "A lower LD50 indicates increased toxicity.", style=styles['para-txt']),
            html.P('P.E. - Point Estimate \n L.B. - Lower Bound \n U.B. - Upper Bound', style=styles['para-txt']),
        ], id='ld50-abbv-div', style=styles['abbv-div']),

        html.Div([
            html.P(" Infection Unit ", style=styles['default-para-head']),
            html.P("CCID50 - Cell Culture Infectious Dose 50% \n EID50 - Egg Infective Dose 50% \n FFU - Focus-forming Unit \n" + 
                    "PFU - Plaque-Forming Unit \n TCID50 - Tissue Culture Infectious Dose 50% ", style=styles['para-txt']),
        ], id='ifu-abbv-div', style=styles['abbv-div']),

        html.Div([
            html.P(" DISPOT - Domain Interaction Statistical POTential ", style=styles['default-para-head']),
            html.P("A more negative score indicates higher likelihood of interactions.", style=styles['para-txt']),
        ], id='dispot-abbv-div', style=styles['abbv-div']),

        html.Div([
                html.P(" Note ", style=styles['default-para-head']), 
                html.P("Pink Nodes represent Virus Protein Segments \n Blue Nodes represent Mouse Protein Domains", style=styles['para-txt']),
                html.P("A thicker edge represents a more negative DISPOT Statistical Potential Score.", style=styles['para-txt'])
        ], id='note-abbv-div', style=styles['abbv-div'])
    )

    return abbv_content

## Return Non-interacting/Uniprot ID NOT FOUND viral protein domains (datatable)
@app.callback(
    Output('no-int-info-div', 'children'),
    Input('store-taxonomy', 'data') ## Get Taxonomy ID
)
def rtn_no_int(tax_accession):

    ## Filter dataframes
    f_uni = v_uni[v_uni['TaxonomyID']==tax_accession]
    f_domains = all_domains[all_domains['TaxonomyID']==tax_accession]
    f_int = interact_df[interact_df['TaxonomyID']==tax_accession]

    ## Change vFamilyID to string
    f_df = pd.merge(f_uni, f_domains, on=['TaxonomyID', 'Segment', 'UniProt_ID'], how='left').fillna('N/A')
    f_new_noint = f_df[~f_df.vFamilyID.isin(f_int.vFamilyID)].reset_index(drop=True)

    f_new_noint = f_new_noint.drop(columns=['TaxonomyID'])
    f_new_noint['vFamilyID'] = f_new_noint['vFamilyID'].astype(str).str.split('.').str[0]

    f_new_noint.columns = ['Segment', 'UniProt ID', 'SCOP Superfamily ID', 'Superfamily', 'SCOP Start/End Residue(s)']

    return dash_table.DataTable(
        
        data = f_new_noint.to_dict('records'),
        columns = [{"name": i, "id": i} for i in f_new_noint.columns],
        style_cell={'textAlign': 'left'},
        style_header=styles['default-style-header'],
        style_data=styles['default-style-data'],
        style_cell_conditional=[ ## disable highlighting of active cell
            {
                'if' : {'state':'selected'},
                'backgroundColor' : 'inherit !important',
                'border' : 'inherit !important'
            },
        ],
        fill_width=False,
    )

## Return protein sequence
@app.callback(
    [Output('v-seq-div', 'children'), 
    Output('m-seq-div', 'children')],
    [Input('chosen-protein', 'value'),
    Input('store-v-node', 'data')]
)
def rtn_protein_seq(chosen_protein, v_node_uniprot):
    v_uni = ""
    v_seq = ""
    m_uni = ""
    m_seq = ""

    ## Virus protein sequence
    if v_node_uniprot:
        v_url = "https://www.uniprot.org/uniprot/" + v_node_uniprot + ".fasta"
        v_page = requests.get(v_url)
        v_soup = BeautifulSoup(v_page.content, 'html.parser')
        v_get_seq = v_soup.get_text()
        v_seq = ''.join(v_get_seq.splitlines(keepends=False)[1:]) # Splits at space
    
    else:
        v_uni = "Select a Virus (Pink) Node" ## Show 'instructions'

    ## Mouse protein sequence
    if chosen_protein:
        mSuperfamily_df=df_mp.loc[df_mp['Protein']==chosen_protein]
        # print(mSuperfamily_df)
        # SCOP_residue_string=mSuperfamily_df['mSCOP'].to_string(index=False)

        ## --> return to m-uni-id children
        m_uni = mSuperfamily_df['UniprotID'].values[0]

        ## Retrieve Protein Sequence String here
        m_url = "https://www.uniprot.org/uniprot/" + m_uni + ".fasta"
        m_page = requests.get(m_url)
        m_soup = BeautifulSoup(m_page.content, 'html.parser')
        m_get_seq = m_soup.get_text()
        m_seq = ''.join(m_get_seq.splitlines(keepends=False)[1:]) # Splits at space
    
    else:
        m_uni = "Select mouse protein from Browse Proteins dropdown" ## Show 'instructions'

    return (
        (html.P(v_uni, style=styles['default-para-head']),
        html.P(v_seq, style=styles['seq-txt'])),

        (html.P(m_uni, style=styles['default-para-head']),
        html.P(m_seq, style=styles['seq-txt'])),
    )

@app.callback(
    [Output('footer-sub-header', 'children'),
    Output('footer-div-content', 'children')],
    Input('no-int-btn', 'n_clicks'),
    Input('abbrv-btn', 'n_clicks'),
    Input('protein-seq-btn', 'n_clicks')
)
def rtn_footer_content(get_int, get_abbrv, get_seq):
    
    ctx = dash.callback_context
    changed_id = [p['prop_id'] for p in ctx.triggered][0]
    # print(changed_id)

    sub_head = ""

    if changed_id=='no-int-btn.n_clicks':
        sub_head = (
            html.H5("Non-interacting Viral Protein Segments", style=styles['default-header']),
        )
        get_content = write_no_int()
    
    elif changed_id=='abbrv-btn.n_clicks':
        sub_head = html.H5("Abbreviations", style=styles['default-header'])
        get_content = write_abbv()
    
    elif changed_id=='protein-seq-btn.n_clicks':
        sub_head = (
            html.H5("Protein Sequence", style=styles['default-header']),
        )
        get_content = write_protein_seq()

    return sub_head, get_content