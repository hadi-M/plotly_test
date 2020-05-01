# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app
import plotly.graph_objects as go
from pdb import set_trace 
import pickle

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# function for loading data file
def load_object(file_name): 
    dbfile = open(file_name, 'rb')
    obj = pickle.load(dbfile)
    dbfile.close()
    return obj


The_What_markdown = \
    """
    ## The What

    """

#### <<<<~~~~----( The Why )----~~~~>>>> ####

The_Why_markdown = \
    """

    ## The Why
    This happens to everyone who is learning coding out there. While learning something new, you just start confirming concepts you just learnt, to see that they really work as they are intended, by
    connecting those concepts to stuff that you've already confirmed, and you are familiar with them.\n
    Here I wanted to confirm the little knowledge I have of finance
    """

The_What_row = dbc.Row(
    [
        dcc.Markdown(
            The_Why_markdown
        ),
        # dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    style={"font-family": "Times New Roman", "font-size": "21px"}
)

 
#### <<<<~~~~----( Tabbed graph 1 )----~~~~>>>> ####

X_all = pd.read_csv("X_all.csv")
y_all = pd.read_csv("y_all.csv")
date_all = pd.read_csv("date_all.csv")

y_test_y_pred_df_dict = load_object("y_test_y_pred_df_dict.pickl")
linear_regression_models_df = load_object("linear_regression_models_df.pickl")
list_of_tabs = []

list_of_publicly_traded_airlines = {
    "UAL": "United Air Lines Inc.",
    "ALK": "Alaska Airlines Inc.",
    "DAL": "Delta Air Lines Inc.",
    "SAVE": "Spirit Air Lines",
    "ALGT": "Allegiant Air",
    "AAL": "American Airlines Inc.",
    "HA": "Hawaiian Airlines Inc.",
    "JBLU": "JetBlue Airways",
    "MESA": "Mesa Airlines Inc.",
    "RYAAY": "Ryan International Airlines",
    "SKYW": "SkyWest Airlines Inc.",
}

for symbol in y_test_y_pred_df_dict.keys():
    # data_tmp = final_data_dict[symbol]
    fig1 = go.Figure()
    show_df = y_test_y_pred_df_dict[symbol]
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y test"], name='predicted'))
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y pred"], name='real'))
    
    fig = dcc.Graph(
                figure={
                    'data': [
                        {'x': show_df.index, 'y': show_df["y test"],
                            'type': 'scatter', 'name': 'Stock Price'},
                        {'x': show_df.index, 'y': show_df["y pred"],
                         'type': 'scatter', 'name': 'Predicted'},
                    ],
                    'layout': {
                        'title': list_of_publicly_traded_airlines[symbol],
                        'xaxis': {
                            'title': 'Date'
                        },
                        'yaxis': {
                            'title': 'y value'
                        }
                    }
                }
            )

    # fig2 = dcc.Graph(id='regression-{}'.format(symbol)),
    # slider2 = dcc.Slider(
    #     id='slider-PASSENGERS_x_DISTANCE-{}'.format(symbol),
    #     min=1,
    #     max=1000,
    #     value=1,
    #     step=100,
    #     marks={i: str(i) for i in range(1, 1000, 100)}
    # )

    # list_of_tabs.append(dbc.Row([dcc.Tab(label=symbol, children=fig2), dcc.Tab(label=symbol, children=fig2)]))
    list_of_tabs.append(
        # dbc.Col([dcc.Tab(label=symbol, value=symbol, children=fig2), slider2])
        dcc.Tab(label=symbol, value=symbol, children=fig)
    )


row3 = dcc.Tabs(list_of_tabs, style={"margin": "auto"})


# fig = go.Figure()
# fig.add_trace(go.Scatter(x=date_all.Date, y=y_all.Close, name='y_pred_all'))

# column4 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )


# gapminder = px.data.gapminder()
# fig_oo = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dcc.Markdown('''

Inline code snippet: `True`

Block code snippet:
```py
import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```
''')

# row3 = dbc.Row(
#     [
#         dcc.Markdown('Dash converts Python classes into HTML')
#     ]#, style={"display": "block"}
# )

#################### new code tabs:




# row3 = dcc.Tabs(dcc.Tab(fig_oo))

#### <<<<~~~~----( The What )----~~~~>>>> ####



layout = [The_What_row, row3, column2, column2]