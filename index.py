from dash import  dcc, html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import USA, Europe


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('EV sales in USA          |      ', href='/apps/USA'),
        dcc.Link('EV sales in Europe      |      ', href='/apps/Europe'),
        ], className="row"),
    html.Div(id='page-content', children=[])
    ])


@app.callback(Output('page-content', 'children'),
        [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/USA':
        return USA.layout
    if pathname == '/apps/Europe':
        return Europe.layout
    else:
        return "Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)
