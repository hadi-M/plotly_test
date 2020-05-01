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
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Row(
    [
        dcc.Markdown(
            """
        
            ## The Why
            This happens to everyone who is learning coding out there. While learning something new, you just
            start confirming concepts you just learnt, to see that they really work as they are intended, by
            connecting those concepts to stuff that you've already confirmed, and you are familiar with them.
            """
        ),
        # dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    style={"font-family": "Times New Roman"}
)


X_all = pd.read_csv("X_all.csv")
y_all = pd.read_csv("y_all.csv")
date_all = pd.read_csv("date_all.csv")

# lr2 = LinearRegression()
# lr2.fit(X_all, y_all)

# y_pred_all = lr2.predict(X_all)



fig = go.Figure()

# show_df = pd.DataFrame({"y test": y_test.values, "y pred": y_pred}, index=test_date.values)
fig.add_trace(go.Scatter(x=date_all.Date, y=y_all.Close, name='y_pred_all'))
# fig.add_trace(go.Scatter(x=date_all, y=y_all, name='y real'))
# set_trace()
column4 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)


# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
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

row3 = dbc.Row(
    [
        dcc.Markdown('Dash converts Python classes into HTML')
    ]#, style={"display": "block"}
)

layout = dbc.Row([column1, column4, row3], style={"max-width": "800"})