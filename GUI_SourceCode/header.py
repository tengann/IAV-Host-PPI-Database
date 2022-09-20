from maindash import app
import pandas as pd
import dash
from dash import dash_table
from dash import html
from dash import dcc

from dash.dependencies import Input, Output

from styles import styles

df = pd.read_csv("./excel/pathogen_info.csv")

def displayPathogen():
    return html.Div(id='pathogen-header',style=styles['pathogen-header'])

def displayInfoTable():
    return html.Div(id='info-table', style=styles['info-table'])

# @app.callback(
#     Output('pathogen-header','children'),
#     Input('store-pathogen', 'data')
# )
# def pathogenInfoTable(chosen_pathogen):
#     print(chosen_pathogen)
#     dff=df[df.Pathogen==chosen_pathogen]
#     return dff.Subtype.unique()+ " - " + dff.Pathogen.unique() + "\nTaxonomy ID: " + str(dff.TaxonomyID.unique())

'''
    Return selected pathogen to 'pathogen-header'
    Return LD50 info to table
'''
@app.callback(
    
    [Output('pathogen-header','children'), 
    Output('info-table','children')], 
    Input('store-pathogen', 'data')
)
def pathogenInfoTable(chosen_pathogen):
    
    dff=df[df.Pathogen==chosen_pathogen]
    pathogenInfo_df=dff.drop(columns=['Pathogen', 'TaxonomyID', 'Subtype'])
    
    tax_id = dff['TaxonomyID'].unique()[0] ## unique() changes dataframe to array
    # print(tax_id) 
    
    columns = [
        {'name':['', 'PubMed ID'], 'id':'Pubmed ID'},
        {'name':['', 'Mouse Genome'], 'id':'Mouse Genome'},
        {'name':['', 'LD50'], 'id':'Lethal Dose 50 (LD50)'},
        {'name':['', 'Infection Unit'], 'id':'Infection unit'},
        {'name':['Virulence Level', 'Two-class'], 'id':'Two-class Virulence Level'},
        {'name':['Virulence Level', 'Three-class'], 'id':'Three-class Virulence Level'},
    ]
    data = pathogenInfo_df.to_dict('records')

    return (
        
        (dff.Subtype.unique()+ " - " + dff.Pathogen.unique() + "\nTaxonomy ID: " + str(dff.TaxonomyID.unique())),
        
        dash_table.DataTable(
            data=data, columns=columns, 
            merge_duplicate_headers=True,
            style_cell={'textAlign': 'left'},
            style_header=styles['default-style-header'],
            style_data=styles['default-style-data'],
            style_cell_conditional=[ ## disable highlighting of active cell
                {
                    'if' : {'state':'selected'},
                    'backgroundColor' : 'inherit !important',
                    'border' : 'inherit !important'
                }
            ],
            fill_width=False,
        ),
    )