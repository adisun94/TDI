from app import app
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup
import seaborn as sns

evdata=pd.read_json('/home/adisun/dash-app/EV/EV-sales-data/Europe-EV.json', orient='records')

#app = Dash(__name__)

layout = html.Div([

    html.Div(children=[
        dcc.Graph(
            id='europe_corrmap', 
            figure={},
            hoverData={'points':[{'x':'Battery(kWh)','y':'Battery(kWh)'}]}
            ),       
        dcc.Graph(
            id='europe_pair',
            figure={}
            )
        ],
        style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        dcc.Dropdown(
            evdata.columns[1:],'Make',
            id='europe_hist'
            ),
        dcc.Graph(
            id='hist_map',
            figure={}
            )
        ], 
        style={'padding': 10, 'flex': 1})

    ],
    style={'display': 'flex', 'flex-direction': 'row'})

@app.callback(
    Output('europe_corrmap','figure'),
    Output('europe_pair','figure'),
    Input('europe_corrmap', 'hoverData')
    )
def update_output(hoverData):
    print(hoverData)
    fig=px.imshow(evdata.drop(columns=['Name']).corr().round(3),title="Correlations between features in the dataset for EV in Europe")
    fig.update_layout(
            title_x=0.5,
            title_font=dict(size=16),
            margin=dict(t=50, b=0,r=0,  l=0)
            )
    fig.update_layout(coloraxis_colorbar_x=0.8)

    fig2 = go.Figure(data=px.scatter(
        x=evdata[hoverData['points'][0]['x']], 
        y=evdata[hoverData['points'][0]['y']],
        color=evdata['Make']
        )
        )


    # Create x and y buttons
   # x_buttons = []
   # y_buttons = []

   # for ncol,rcol in zip(evnumber.columns, evnumber.columns[::-1]):
   #     x_buttons.append(dict(method='update',
   #         label=ncol,
   #         args=[{'x': [evnumber[ncol]],'color':'black'}]
   #         )
   #         )

    #    y_buttons.append(dict(method='update',
    #        label=ncol,
    #        args=[{'y': [evnumber[ncol]]}]
    #        )
    #        )

    # Pass buttons to the updatemenus argument
    fig2.update_layout(width=600,height=500)


    return fig, fig2

@app.callback(
    Output('hist_map', 'figure'),
    Input('europe_hist','value'))
def update_y_timeseries(value):
    fig = go.Figure(px.histogram(x=evdata[value],
                                 labels={'x':''},
                                 title=value).update_xaxes(categoryorder='total descending'))
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    fig.update_layout(
            width=600,height=500,
            title_x=0.5,title_y=0.01,
            title_font=dict(size=16),
            margin=dict(t=50, b=0,r=0,  l=0),
            font=dict(size=14))

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

