from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from glob import glob
import numpy as np
import pandas as pd
import pathlib
from app import app

layout = html.Div([
    dcc.Markdown('''
        ## Electric vehicles (EVs) are predicted to be an integral part of modern, sustainable economies.  Replacing combustion engines with batteries reduces our carbon footprint and improves air quality. However, the current costs associated with researching & manufacturing batteries makes EVs more expensive. As such, it is crucial for the buyer to be informed about the pros and cons of purchasing EVs. This app is intended to help vehicle buyers make informed selections of EVs, by providing 1) interactive dashboards to explore the performance metrics of commercial EVs and 2) models to estimate vehicle costs.'''),
    html.Br(),
    dcc.Markdown('''
        ### The first dashboard 'EV sales in USA' contains visualizations to show state-wise EV sales in the United States, from 2010-2022. The data is scraped from the [Atlas EV Hub](https://www.atlasevhub.com/materials/state-ev-registration-data/#data).'''),
    html.Br(),
    dcc.Markdown('''
        ### The second dashboard 'EV sales in Europe' contains visualizations to show EV available in Europe. The data is scraped from the [Electric Vehicle Database](https://ev-database.org/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~450|range-slider-battery:prev~next=10~200|range-slider-towweight:prev~next=0~2500|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=9).''')
    ],
    style={'padding': 10, 'flex': 1, 'background-color' : 'rgb(255,255,240)'})
