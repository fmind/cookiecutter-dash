#!/usr/bin/env python3

"""Interactive dashboards."""

import dash
import dash_core_components as dcc
import dash_html_components as html

APP = dash.Dash(__name__)

APP.layout = html.Div(children=[
    html.H1(
        children='Hello Dash!'
    ),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    APP.run_server(debug=True)
