from styles import styles
from dash import html
from dash import dcc

def create_contact_page():

    return html.Div([

        html.Div([
            
            html.Div([
                html.P('Designed and developed by:\n' +
                    'Ng Teng Ann\n' + 
                    'tengann.ng@ntu.edu.sg\n' +
                    '\n' + 
                    'Shamima Rashid\n' + 
                    'bshamima@ntu.edu.sg\n' +
                    '\n\n' + 
                    'Correspondence:\n' + 
                    'Chee Keong Kwoh\n' + 
                    'asckkwoh@ntu.edu.sg\n', style=styles['para-txt']),
            ], style=styles['contacts-sub-container']),

            html.Div([
                html.P('Biomedical Informatics Lab\n' + 
                        'School of Computer Science and Engineering\n' + 
                        'Nanyang Technological University\n' + 
                        'Block NS4-04-33\n' + 
                        '50 Nanyang Avenue\n' + 
                        'Singapore 639798', style=styles['para-txt']),

            ], style=styles['contacts-sub-container']),

        ], style=styles['contacts-main-container']),
        
        html.Div([
            html.P('If you use IAV-Mouse PPI web server as part of your workflow, please consider citing our paper: \n' + 
                'T. A. Ng, S. Rashid, and C. K. Kwoh, "Virulence Network of Interacting Influenza-Host Protein Domains," bioRxiv, p. 2022.10.11.511722, 2022, doi: 10.1101/2022.10.11.511722.'
                , style=styles['para-txt']),
            html.P('Last updated: 12 January 2023', style=styles['para-txt']),
        ], style=styles['contacts-sub-container']),
    ])