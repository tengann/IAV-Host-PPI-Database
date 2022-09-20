from maindash import app
import pandas as pd
import dash
from dash import html
from dash import dcc

from dash.dependencies import Input, Output

from styles import styles

df = pd.read_csv("./excel/pathogen_info.csv")

## Cascading dropdown
def dropdown_func():
    return html.Div([

        html.Div([
            html.Label("Select Subtype: ", style=styles['home-label']),
            # html.Label("Select Subtype: "),
            dcc.Dropdown(id='subtype-choice', 
                        options=[{'label':s, 'value':s} for s in sorted (df.Subtype.unique())],
                        clearable=False,
                        value='H1N1',#Default Value
                        style=styles['home-dropdown']
            ),
        ]),

        html.Div([
            html.Label("Select Pathogen: ", style=styles['home-label']),
            dcc.Dropdown(id='pathogen-choice', 
                        options={}, #options populated from Callback
                        clearable=False,
                        value='A/Puerto Rico/8/1934',
                        style=styles['home-dropdown']
            ), 
        ], style = {'margin-top':'10px'})
    ], style={'width':'50%'})

# Populate options of Pathogen dropdown based on Subtypes dropdown
@app.callback(
    Output('pathogen-choice','options'),
    Input('subtype-choice', 'value')
)
def filterPathogenOpts(chosen_subtype):
    pathogen_df=df[df.Subtype==chosen_subtype]
    return [{'label':p, 'value':p} for p in sorted(pathogen_df.Pathogen.unique())]

## Get data 
@app.callback(
    [Output('store-pathogen', 'data'),
    Output('store-taxonomy', 'data')], ## Store Taxonomy ID
    Input('pathogen-choice', 'value')
    # prevent_initial_call=True, # prevent callbacks from firing their inputs initially appear in the layout of app
)
def load_store(chosen_pathogen):

    df_filter = df[df['Pathogen']==chosen_pathogen]
    tax_id = df_filter['TaxonomyID'].unique()[0]
    
    return chosen_pathogen, tax_id