from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import plotly.express as px
import pandas as pd

dash_app = Dash()
app =  dash_app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.DataFrame({
#    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#    "Amount": [4, 1, 2, 2, 4, 5],
#    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})
df = pd.read_csv("fruits.csv")
print(list(df.columns))
print(df)

fig = px.bar(df, x=df.columns[0], y=df.columns[1], color=df.columns[2], barmode="group")

dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for your data.'''),
    dcc.Graph(id='example-graph',figure=fig),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic', children='Enter a value and press submit')
])

             
@dash_app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(value,n_clicks)             
             
             
if __name__ == '__main__':
    dash_app.run_server(debug=True,use_reloader=False)
