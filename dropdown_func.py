from maindash import app
import pandas as pd
import dash
from dash import html
from dash import dcc

from dash.dependencies import Input, Output

from styles import styles

df = pd.read_csv("./excel/pathogen_info.csv")

def dropdown_func():
    return html.Div([

        html.Div([
            html.Label("Select Subtype: ", style=styles['home-label']),
            dcc.Dropdown(id='subtype-choice', 
                        options=[{'label':s, 'value':s} for s in sorted (df.Subtype.unique())],
                        clearable=False,
                        value='H1N1',
                        style=styles['home-dropdown']
            ),
        ]),

        html.Div([
            html.Label("Select Pathogen: ", style=styles['home-label']),
            dcc.Dropdown(id='pathogen-choice', 
                        options={}, 
                        clearable=False,
                        value='A/Puerto Rico/8/1934',
                        style=styles['home-dropdown']
            ), 
        ], style = {'margin-top':'10px'})
    ], style={'width':'50%'})

@app.callback(
    Output('pathogen-choice','options'),
    Input('subtype-choice', 'value')
)
def filterPathogenOpts(chosen_subtype):
    pathogen_df=df[df.Subtype==chosen_subtype]
    return [{'label':p, 'value':p} for p in sorted(pathogen_df.Pathogen.unique())]

## Get data 
@app.callback(
    Output('store-pathogen', 'data'),
    Input('pathogen-choice', 'value')
)
def load_store(chosen_pathogen):
    return chosen_pathogen
