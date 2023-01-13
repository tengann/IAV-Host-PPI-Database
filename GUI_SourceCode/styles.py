### margin ## top/bottom   left/right (w/ respect to Parent Div)

### 'display' : 'flex', #! important to use justify-content/align-items
### 'justify-content' : 'center', ## center horizontally
### 'align-items' : 'center', ## center vertically
### 'padding' ### (within Div)

styles = {
    
    ### Standard styles
    'webpage' : {
        'width' : '100%',
        'height' : 'auto',
        'color' : '#323232', ## text colour
        'font-family' : 'Helvetica, sans-serif',
        'display' : 'flex',
        'flex-direction' : 'column',
        'justify-content' : 'center', 
    },

    ### Format text
    'default-header':{ ## define standard for all headers
        'font-family' : 'Verdana, sans-serif',
        'font-weight' : 'bold',
    },

    ## Paragraph header
    'default-para-head':{
        'font-family' : 'Helvetica, sans-serif',
        'font-size' : '14px',
        'font-weight' : 'bold',
    },
    ## Paragraph text
    'para-txt':{
        'font-family' : 'Helvetica, sans-serif',
        'font-size' : '12px',
        'white-space': 'pre-line',
    },

    ### Homepage
    'home-page-container':{
        'margin-top':'10px',
        'display' : 'flex', 
        'flex-direction' : 'column',
        'justify-content' : 'center', 
        'align-items' : 'center', 
        'margin' : 'auto 25%', 
    },

    'icon-container':{
        'width': '50%',
        'margin': '10px auto', ## *
        'padding' : '20px', ## *
        'display' : 'flex',
        'flex-direction' : 'column',
        'justify-content' : 'center',
        'align-items' : 'center',
        # 'border': '2px black dashed',
    },

    'home-label':{
        'display': 'inline-block',
        'vertical-align': 'middle',
        'font-weight' : 'bold',
        'font-size' : '14px',
    },

    'home-dropdown':{
        'height': '40px', 
        'vertical-align': 'middle',
        'font-size' : '14px',
    },

    'home-txt':{
        'font-family' : 'Helvetica, sans-serif',
        'font-weight' : 'bold',
        'font-size' : '14px',
        'white-space': 'pre-line', 
        'display': 'inline-block',
        'vertical-align': 'middle',
    },

    'label':{
        'width':'85%',
        'display': 'inline-block',
        'vertical-align': 'middle',
        'font-weight' : 'bold',
        'font-size' : '14px',
    },

    'dropdown':{
        'width': '85%', 
        'height': '40px', 
        'vertical-align': 'middle',
        'font-size' : '14px',
    },

    'organ-dropdown':{
        'width' : '90%', ## Increased width
        'height': '40px', 
        'vertical-align': 'middle',
        'font-size' : '14px',
    },

    ### Main-page
    ### Consist of header, body and footer
    'main-container':{ 
        'margin' : '0 auto',
        'width' : '100%',
        'postion' : 'relative', 
        'display' : 'flex',
        'flex-direction' : 'column',
    },

    ## Navigation bar
    'nav-bar':{
        'width' : '100%',
        'backgroundColor' : '#323232', ## correspond to LD50 info-table
        'display':'flex',
        'align-items' : 'center',
        # 'padding' : '20px',
    },

    ## Centre: Header
    'nav-bar-header-div':{
        'width' : '56%',
        'color': 'white',
        'textAlign': 'center',
        'font-style' : 'italic',
        # 'border':'2px solid white',
    },

    ## Left: Placeholder
    'nav-bar-L-sub-div':{ 
        'width' : '22%', 
        # 'border':'2px solid white',
    },

    ## Right: Button(s)
    'nav-bar-R-sub-div':{
        'width' : '22%',
        'display':'flex',
        'align-items' : 'center',
        # 'border':'2px solid white',
    },

    'nav-bar-btn-div':{ ## In 'nav-bar-R-sub-div'
        'padding' : '10px',
        # 'border':'2px solid #99DDCC',
    },

    'nav-bar-btn':{
        'background-color' : '#97B3D0',
        'color':'#323232',
        'font-size' : '14px',
        'font-weight' : 'bold',
        'padding' : '12px 28px',
        'border-radius':'8px', ## rounded buttons
        'border':'2px solid #99DDCC',
        'margin-left':'10px',
    },

    'header':{ ## Container for pathogen-header and LD50 info table
        'margin' : '10px auto', ## Used for Centering blocks
    },

    'body':{ ### Consist of left-panel and right-panel
        # 'border': '2px #9DC183 solid',
        'margin' : '10px auto', ## top/bottom   left/right
        'width' : '90%',
        'display' : 'flex',
    },

    'footer':{
        # 'border': '2px #9DC183 solid',
        'margin' : '10px auto',
        'width' : '90%',
    },
    
    ### Header
    'pathogen-header':{
        'border': '2px #99DDCC solid', 
        'backgroundColor' : '#CA8EB0',
        'margin' : '25px',
        'padding' : '20px',
        'height' : '90px',
        'textAlign' : 'center',
        'vertical-align' : 'middle',
        'line-height': '25px',
        'font-size' : '20px',
        'font-weight' : 'bold',
        'white-space': 'pre-line', ## for newline
    },

    'info-table':{
        # 'position' : 'relative',
        'border': '2px #97B3D0 dashed', ## Placeholder border
        'margin' : '15px auto', ## top/bottom   left/right
        'padding' : '10px', ## for contents
        # 'height' : '150px',
        'display' : 'flex',
        'justify-content' : 'center', ## center horizontally
        'align-items' : 'center', ## center vertically
        # 'overflow': 'auto',
    },

    ### Body
    'left-panel':{
        # 'border': '2px #9898C9 solid',
        'width' : '68%',
        'float':'left',
    },

    'right-panel':{
        # 'border': '2px #9898C9 solid',
        'width' : '30%',
        'float':'right',
        'margin-left' : '2%',
        'display' : 'flex', 
        'flex-direction' : 'column',
    },
    
    ## Left panel
    'network-graph-div':{
        'border': '2px #97B3D0 dashed',
        'margin' : '30px auto 15px auto',  ## top right bottom left
        'padding' : '10px', 
        'vertical-align' : 'center', ## div
        'display' : 'flex', #! important to use justify-content/align-items
        'flex-direction' : 'column',
        'justify-content' : 'center', ## center horizontally
        'align-items' : 'center', ## center vertically
    },

    ### Within network-graph-div
    'display-graph':{
        # 'border' : '2px dotted #99DDCC',
        'margin' : '15px',
        'padding' : '10px',
        'overflow': 'auto',
    },

    'edge-info-wrapper':{
        'border' : '2px dotted #99DDCC',
        'margin' : '15px',
        'padding' : '10px',
        'width' : '90%',
        'position' : 'relative',
        'display' : 'flex',
        'flex-direction' : 'column',
        'justify-content' : 'center',
    },

    'edge-info':{
        # 'border' : '2px dotted #99DDCC',
        'margin' : '5px',
        # 'width' : '90%',
        'position' : 'relative',
        'display' : 'flex',
        'justify-content' : 'center', 
        'align-items' : 'center', 
        # 'white-space': 'pre-line'
    }, 
    
    'node-info':{ 
        'border' : '2px #97B3D0 dashed', # cornflower blue
        # 'margin' : '15px auto',
        # 'height' : '500px',
        'padding' : '10px',
        # 'width' : '90%'
    },
    
    'node-table-div':{
        'margin': '15px auto',
        'overflow': 'auto',
    },

    ### Footer 
    'footer-sub-head-div':{
        'margin': '10px auto',
        'padding' : '20px',
        'display':'flex',
        'flex-direction' : 'column',
        'justify-content' : 'center',
        'align-items' : 'center', 
    },

    'footer-sub-div':{
        'margin': '10px auto',
        'padding' : '20px',
        'display':'flex',
        'justify-content' : 'center'
    },

    'seq-header-div':{
        'margin':'10px auto',
        'padding':'10px',
        # 'height': '60px',
        'white-space': 'pre-line',
    },

    'seq-sub-div':{
        # 'border' : '2px dotted #99DDCC',
        'margin':'10px auto',
        'padding':'10px',
        'white-space': 'pre-line',
    },

    'seq-div': {
        'border':'2px #97B3D0 dashed',
        'margin':'15px auto',
        'padding':'10px',
        'white-space': 'pre-line',
        'width': '48%'
    },

    'seq-txt':{
        'font-family' : 'Helvetica, sans-serif',
        'font-size' : '12px',
        'white-space': 'pre-line',
        'word-wrap': 'break-word',
        'word-break': 'break-word',
    },
                                      
    'abbv-div':{
        'border': '2px #97B3D0 dashed',
        'margin' : '15px auto',
        'padding' : '10px',
        # 'height' : '150px',
        'white-space': 'pre-line',
        'width': '33%'
    },

    ## Data table (LD50 table & Non-int table)
    'default-style-header':{
        'backgroundColor': '#97B3D0', 
        'border' : '2px solid #99DDCC',
        'font-family' : 'Helvetica, sans-serif',
        'font-weight' : 'bold',
        'textAlign': 'center'
    },

    'default-style-data':{
        'backgroundColor': '#323232', 
        'color': 'white',
        'border' : '2px solid #99DDCC',
        'font-family' : 'Helvetica, sans-serif',
        'font-size' : '14px'
    },

    ## Data table (node info & edge info)
    'style-data':{
        'border' : '2px solid #99DDCC',
        'font-family' : 'Helvetica, sans-serif',
        'font-size' : '14px'
    },

    ## Button
    'btn': {
        'background-color' : '#97B3D0',
        'color':'#323232',
        'font-size' : '14px',
        'font-weight' : 'bold',
        'padding' : '12px 28px',
        'border-radius':'8px', ## rounded buttons
        'border':'2px solid #99DDCC',
        'height' : '70px',
        'width' : '180px'
    },

    ## Contact Page
    'contacts-main-container':{
        'margin-top':'20px',
        'margin': '10px auto',
        'padding' : '20px',
        'display':'flex',
        'justify-content' : 'center',
        'width' : '100%',
        'backgroundColor' : '#323232',
        'color': 'white',
    },

    'contacts-sub-container':{
        'margin' : '10% 25%',
        'display' : 'flex',
        'flex-direction' : 'column',
        'justify-content' : 'center',
        'align-items' : 'center',
        'text-align': 'center',
        'margin' : '15px auto',
        'padding' : '10px',
        'white-space': 'pre-line',
        'width': '50%',
        # 'border': '2px white dashed',
    }, 

    ### Help page
    'hp-L-main-div':{
        'float':'left',
        'width':'50%',
        'display' : 'flex',
        'flex-direction':'column',
        'justify-content' : 'center', 
        'align-items' : 'center', 
        'padding' : '10px', 
        # 'border': '2px pink dashed',
    },

    'hp-R-main-div':{
        'float':'right',
        'width':'50%',
        'display' : 'flex',
        'flex-direction':'column',
        'justify-content' : 'center', 
        'align-items' : 'center', 
        'padding' : '10px', 
        # 'border': '2px pink dashed',
    },

    'hp-content-header-div':{
        'width':'95%',
        'height':'10%',
        'text-align': 'center',
        'border': '2px #99DDCC dashed', ## pink
    },

    ## For descriptions
    'hp-LR-content-top-div':{
        'width':'95%',
        'height':'18%', ## 18%
        'margin-top':'10px',
        'border': '2px #97B3D0 dashed', ## blue
        'font-size' : '20px',
        'font-weight' : 'bold',
        'white-space' : 'pre-line',
    },

    ## For Links 
    'hp-L-content-btm-div':{
        'width':'95%',
        'margin-top':'10px',
        'border': '2px #97B3D0 dashed', ## blue
    },

    ## For flowchart
    'hp-R-content-btm-div':{
        'width':'95%',
        # 'height':'70%',
        'margin-top':'10px',
        'display' : 'flex',
        'justify-content' : 'center', 
        'align-items' : 'center', 
        'overflow': 'auto',
        'border': '2px #97B3D0 dashed', ## blue
    }
}