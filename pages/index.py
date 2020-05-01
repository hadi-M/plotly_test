# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app
import plotly.graph_objects as go
from pdb import set_trace
import pickle

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# function for loading data file
def load_object(file_name): 
    dbfile = open(file_name, 'rb')
    obj = pickle.load(dbfile)
    dbfile.close()
    return obj


The_Abstract_markdown = \
    """
    ## The Abstract
    In this post I wanted to check if the airlines' industry of stock market is rational or not.
    By "rational" here, I mean to check if the earning of the airline is reflected on the price of the stock or not.
    \n My data is monthly based and I have 3 features:
    * Sum of the distance of all passenger travelled for each month
    * Sum of the distance of all mails that was moved for each month
    * Sum of the distance of all freight (cargo) travelled for each month

    """

#### <<<<~~~~----( The Why )----~~~~>>>> ####

The_Why_markdown = \
    """

    ## The Why
    This happens to everyone who is learning coding out there. While learning something new, you just start confirming concepts you just learnt, to see that they really work as they are intended, by
    connecting those concepts to stuff that you've already confirmed, and you are familiar with them.\n
    Here I wanted to confirm the little knowledge I have of finance by using regression.
    """

The_Abstract_row = dbc.Row(
    [
        dcc.Markdown(
            The_Abstract_markdown
        ),
        # dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    style={"font-family": "Times New Roman", "font-size": "21px"}
)

#### <<<<~~~~----( The Why )----~~~~>>>> ####

The_How_markdown = \
    """

    ## The How
    So my hypothesis was that stock market is rational and based on the earnings of each airline, it moves accordingly.
    I downloaded the monthly flight data from [bureau of transportation statistics]("https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=308").
    I could download them by manually but I used selenium to download the files automatically, eventhough it took more time. It was neater.
    Then I unzipped them, and merged them via code, so basically just running my python notebook file, would give you all the data and the models.
    \n 
    After reading the data and cleaning it
    Then since each airline has multiple flights per month, I grouped the whole dataset based on carrier name, year nad month.
    then created a 
    
    """

The_Abstract_row = dbc.Row(
    [
        dcc.Markdown(
            The_Abstract_markdown
        ),
        # dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    style={"font-family": "Times New Roman", "font-size": "21px"}
)

 
#### <<<<~~~~----( Tabbed graph 1 )----~~~~>>>> ####

X_all = pd.read_csv("X_all.csv", index_col=False).drop("Unnamed: 0", axis=1)
y_all = pd.read_csv("y_all.csv", index_col=False).drop("Unnamed: 0", axis=1)

date_all = pd.read_csv("date_all.csv", index_col=False).drop("Unnamed: 0", axis=1)
# set_trace()
date_all = pd.to_datetime(date_all["Date"], infer_datetime_format=True)

y_test_y_pred_df_dict_linear_regression = load_object("./y_test_y_pred_df_dict_linear_regression.pickl")
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

for symbol in y_test_y_pred_df_dict_linear_regression.keys():
    # data_tmp = final_data_dict[symbol]
    # fig1 = go.Figure()
    show_df = y_test_y_pred_df_dict_linear_regression[symbol]
    lr_model = linear_regression_models_df[symbol]
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y test"], name='predicted'))
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y pred"], name='real'))
    
    fig1 = dcc.Graph(
                figure={
                    'data': [
                        {'x': show_df.index, 'y': show_df["y test"].values,
                            'type': 'scatter', 'name': 'Stock Price'},
                        {'x': show_df.index, 'y': show_df["y pred"],
                         'type': 'scatter', 'name': 'Predicted'},
                        {'x': show_df.index, 'y': [show_df["y test"].mean()]*len(show_df["y pred"]),
                         'type': 'scatter', 'name': 'Mean'},
                    ],
                    # 'data': [
                    #     {'x': show_df.index, 'y': show_df["y test"],
                    #         'type': 'scatter', 'name': 'Stock Price'},
                    #     {'x': show_df.index, 'y': show_df["y pred"],
                    #      'type': 'scatter', 'name': 'Predicted'},
                    #     {'x': show_df.index, 'y': [show_df["y pred"].mean()]*len(show_df["y pred"]),
                    #      'type': 'scatter', 'name': 'Mean'},
                    # ],
                    'layout': {
                        'title': list_of_publicly_traded_airlines[symbol],
                        'xaxis': {
                            'title': 'Date'
                        },
                        'yaxis': {
                            'title': 'y value'
                        },
                    },
                }
            )
    # set_trace()
    show_df_all = pd.DataFrame({"y test": y_all.values.flatten(), "y pred": lr_model.predict(X_all)}, index=date_all)
    fig2 = dcc.Graph(
                figure={
                    'data': [
                        {'x': show_df_all.index, 'y': show_df_all["y test"].values,
                            'type': 'scatter', 'name': 'Stock Price'},
                        {'x': show_df_all.index, 'y': show_df_all["y pred"],
                         'type': 'scatter', 'name': 'Predicted'},
                        {'x': show_df_all.index, 'y': [show_df_all["y test"].mean()]*len(show_df_all["y pred"]),
                         'type': 'scatter', 'name': 'Mean'},
                    ],
                    # 'data': [
                    #     {'x': show_df.index, 'y': show_df["y test"],
                    #         'type': 'scatter', 'name': 'Stock Price'},
                    #     {'x': show_df.index, 'y': show_df["y pred"],
                    #      'type': 'scatter', 'name': 'Predicted'},
                    #     {'x': show_df.index, 'y': [show_df["y pred"].mean()]*len(show_df["y pred"]),
                    #      'type': 'scatter', 'name': 'Mean'},
                    # ],
                    'layout': {
                        'title': list_of_publicly_traded_airlines[symbol],
                        'xaxis': {
                            'title': 'Date'
                        },
                        'yaxis': {
                            'title': 'y value'
                        },
                    },
                }
            )

    table_columns1 = [
        "Baseline mean, MAE",
        "Baseline mean, MSE",
        "Baseline median, MAE",
        "Baseline median, MSE",
        "After modeling, MAE",
        "After modeling, MSE",
        "After modeling, R2"
        ]
    # set_trace()
    table_data1 = [
        {
            "Baseline mean, MAE": mean_absolute_error(show_df["y test"], [show_df["y test"].mean()]*len(show_df["y test"])),
            "Baseline mean, MSE": mean_squared_error(show_df["y test"], [show_df["y test"].mean()]*len(show_df["y test"])),
            "Baseline median, MAE": mean_absolute_error(show_df["y test"], [show_df["y test"].median()]*len(show_df["y test"])),
            "Baseline median, MSE": mean_squared_error(show_df["y test"], [show_df["y test"].median()]*len(show_df["y test"])),
            "After modeling, MAE": mean_absolute_error(show_df["y test"], show_df["y pred"]),
            "After modeling, MSE": mean_squared_error(show_df["y test"], show_df["y pred"]),
            "After modeling, R2": r2_score(show_df["y test"], show_df["y pred"])
        }
    ]

    table_columns2 = [
        "Baseline mean, MAE",
        "Baseline mean, MSE",
        "Baseline median, MAE",
        "Baseline median, MSE",
        "After modeling, MAE",
        "After modeling, MSE",
        "After modeling, R2"
        ]
    # set_trace()
    table_data2 = [
        {
            "Baseline mean, MAE": mean_absolute_error(show_df_all["y test"], [show_df_all["y test"].mean()]*len(show_df_all["y test"])),
            "Baseline mean, MSE": mean_squared_error(show_df_all["y test"], [show_df_all["y test"].mean()]*len(show_df_all["y test"])),
            "Baseline median, MAE": mean_absolute_error(show_df_all["y test"], [show_df_all["y test"].median()]*len(show_df_all["y test"])),
            "Baseline median, MSE": mean_squared_error(show_df_all["y test"], [show_df_all["y test"].median()]*len(show_df_all["y test"])),
            "After modeling, MAE": mean_absolute_error(show_df_all["y test"], show_df_all["y pred"]),
            "After modeling, MSE": mean_squared_error(show_df_all["y test"], show_df_all["y pred"]),
            "After modeling, R2": r2_score(show_df_all["y test"], show_df_all["y pred"])
        }
    ]

    # table_data = [
    #     {
    #         "Baseline mean, MAE": "2",
    #         "Baseline mean, MSE": "2",
    #         "Baseline median, MAE": "2",
    #         "Baseline median, MSE": "2",
    #         "After modeling, MAE": "2",
    #         "After modeling, MSE": "2",
    #         "After modeling, R2": "2"
    #     }
    # ]

    # table_data = dict(zip(table_columns, table_data))

    list_of_tabs.append(
        # dbc.Col([dcc.Tab(label=symbol, value=symbol, children=fig2), slider2])
        # dcc.Tab(label=symbol, value=symbol, children=fig)
        dcc.Tab(label=symbol, value=symbol, children=dbc.Col(
            [
                fig1,
                # html.Div(
                #     # html.P(correlation, style={"color": "red", "text-align": "center", "font-size": 20}),
                #     html.P("correlation", style={"color": "red", "text-align": "center", "font-size": 20}),
                #     # style={"text"}
                # )

                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in table_columns1],
                    data=table_data1,
                 ),
                fig2,
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in table_columns2],
                    data=table_data2,
                 ),
            ]
        ))
    )


row3 = dcc.Tabs(list_of_tabs, style={"margin": "auto"})

#### <<<<~~~~----( Tabbed graph 2 )----~~~~>>>> ####


y_test_y_pred_df_dict_random_forest = load_object("y_test_y_pred_df_dict_random_forest.pickl")
random_forest_models_df = load_object("random_forest_models_df.pickl")
list_of_tabs = []

for symbol in y_test_y_pred_df_dict_random_forest.keys():
    # data_tmp = final_data_dict[symbol]
    # fig3 = go.Figure()
    rf_model = random_forest_models_df[symbol]
    show_df = y_test_y_pred_df_dict_random_forest[symbol]
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y test"], name='predicted'))
    # fig1.add_trace(go.Scatter(x=show_df.index, y=show_df["y pred"], name='real'))
    # set_trace

    show_df_all = pd.DataFrame({"y test": y_all.values.flatten(), "y pred": rf_model.predict(X_all)}, index=date_all)



    fig3 = dcc.Graph(
                figure={
                    'data': [
                        {'x': show_df.index, 'y': show_df["y test"],
                            'type': 'scatter', 'name': 'Stock Price'},
                        {'x': show_df.index, 'y': show_df["y pred"],
                         'type': 'scatter', 'name': 'Predicted'},
                        {'x': show_df.index, 'y': [show_df["y test"].mean()]*len(show_df["y pred"]),
                         'type': 'scatter', 'name': 'Mean'},
                    ],
                    'layout': {
                        'title': list_of_publicly_traded_airlines[symbol],
                        'xaxis': {
                            'title': 'Date'
                        },
                        'yaxis': {
                            'title': 'y value'
                        },
                    },
                }
            )
    fig4 = dcc.Graph(
            figure={
                'data': [
                    {'x': show_df_all.index, 'y': show_df_all["y test"].values,
                        'type': 'scatter', 'name': 'Stock Price'},
                    {'x': show_df_all.index, 'y': show_df_all["y pred"],
                        'type': 'scatter', 'name': 'Predicted'},
                    {'x': show_df_all.index, 'y': [show_df_all["y test"].mean()]*len(show_df_all["y pred"]),
                        'type': 'scatter', 'name': 'Mean'},
                    ],
                'layout': {
                    'title': list_of_publicly_traded_airlines[symbol],
                    'xaxis': {
                        'title': 'Date'
                    },
                    'yaxis': {
                        'title': 'y value'
                    },
                },
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
    # correlation = corrcoef(show_df["y pred"], show_df["y test"])[0, 1]
    # list_of_tabs.append(dbc.Row([dcc.Tab(label=symbol, children=fig2), dcc.Tab(label=symbol, children=fig2)]))
    table_columns3 = [
        "Baseline mean, MAE",
        "Baseline mean, MSE",
        "Baseline median, MAE",
        "Baseline median, MSE",
        "After modeling, MAE",
        "After modeling, MSE"
        ]
    # set_trace()
    table_data3 = [
        {
            "Baseline mean, MAE": mean_absolute_error(show_df["y test"], [show_df["y test"].mean()]*len(show_df["y test"])),
            "Baseline mean, MSE": mean_squared_error(show_df["y test"], [show_df["y test"].mean()]*len(show_df["y test"])),
            "Baseline median, MAE": mean_absolute_error(show_df["y test"], [show_df["y test"].median()]*len(show_df["y test"])),
            "Baseline median, MSE": mean_squared_error(show_df["y test"], [show_df["y test"].median()]*len(show_df["y test"])),
            "After modeling, MAE": mean_absolute_error(show_df["y test"], show_df["y pred"]),
            "After modeling, MSE": mean_squared_error(show_df["y test"], show_df["y pred"]),
        }
    ]



    # table_data = dict(zip(table_columns, table_data))

    list_of_tabs.append(
        # dbc.Col([dcc.Tab(label=symbol, value=symbol, children=fig2), slider2])
        # dcc.Tab(label=symbol, value=symbol, children=fig)
        dcc.Tab(label=symbol, value=symbol, children=dbc.Col(
            [
                fig3,
                # html.Div(
                #     # html.P(correlation, style={"color": "red", "text-align": "center", "font-size": 20}),
                #     html.P("correlation", style={"color": "red", "text-align": "center", "font-size": 20}),
                #     # style={"text"}
                # )

                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in table_columns3],
                    data=table_data3,
                ),
                fig4,
                # html.Div(
                #     # html.P(correlation, style={"color": "red", "text-align": "center", "font-size": 20}),
                #     html.P("correlation", style={"color": "red", "text-align": "center", "font-size": 20}),
                #     # style={"text"}
                # )

                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in table_columns3],
                    data=table_data3,
                )
            ]
        ))
    )


row4 = dcc.Tabs(list_of_tabs, style={"margin": "auto"})

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



layout = [The_Abstract_row, row3, column2, column2, row4]