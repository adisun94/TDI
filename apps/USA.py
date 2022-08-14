from app import app
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import warnings
warnings.filterwarnings("ignore")
import requests
from bs4 import BeautifulSoup

dtotal=pd.read_json('/home/adisun/dash-app/EV/EV-sales-data/dtotal.json', orient='records')

layout = html.Div([

    html.Div(children=[
        dcc.Graph(
            id='state_sales', 
            figure={},
            hoverData={'points': [{'location': 'MI'}]}),       
        dcc.Slider(
            2000, 2022, 1,
            value=2016,
            id='year',
            marks={i:{'label': str(i), 'style': {'color': '#77b0b1','font-size':'16px'}} for i in range(2000,2023,2)})
        ],
        style={'padding': 10, 'flex': 1, 'background-color' : 'rgb(255,255,240)'}),

    html.Div(children=[
        dcc.Graph(id='car-brand')
        ], 
        style={'padding': 10, 'flex': 1, 'background-color' : 'rgb(255,255,240)'})

    ],
    style={'display': 'flex', 'flex-direction': 'row', 'background-color' : 'rgb(255,255,240)'})

@app.callback(
    Output('state_sales','figure'),
    Input('year', 'value'),
    Input('state_sales','hoverData'))
def update_output(value,hoverData):
    s=dtotal[dtotal['Date']==value]
    fig = go.Figure(
            data=[go.Choropleth(
                locationmode='USA-states',
                locations=s['State'],
                z=s['Count'],
                colorscale='Viridis_r',
                colorbar=dict(thickness=20, ticklen=3,xpad=0,len=0.5,exponentformat='B')
                )]
            )

    fig.update_layout(
            title_text="Cumulative Electric Vehicle sales in the United States",
            title_xanchor="center",
            title_font=dict(size=20),
            title_x=0.5,
            title_y=0.95,
            geo=dict(scope='usa'),
            width=700,
            height=600,
            margin=dict(t=0, b=0,r=100,  l=0))
    fig.update_layout({'paper_bgcolor': 'rgb(255,255,240)', 'plot_bgcolor': 'rgb(255,255,240)'})
            
    fig.update_layout(coloraxis_colorbar_x=-0.1)
    return fig

@app.callback(
    Output('car-brand', 'figure'),
    Input('state_sales', 'hoverData'),
    Input('year','value'))
def update_y_timeseries(hoverData,value):
    n=pd.read_json('/home/adisun/dash-app/EV/EV-sales-data/'+hoverData['points'][0]['location']+'_data.json', orient='records')
    n['Date']=n['Date'].dt.year
    n=n[n['Date']==value]
    n.rename({'Date':'Year'},axis=1, inplace=True)
    fig = px.histogram(n,x='Make', title="New vehicles registered in "+hoverData['points'][0]['location']+' in '+str(value)).update_xaxes(categoryorder='total descending')

    fig.update_layout(width=700,height=500,margin=dict(t=150, b=0,r=0,  l=0))
    fig.update_layout({'paper_bgcolor': 'rgb(255,255,240)', 'plot_bgcolor': 'rgb(255,255,240)'})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

