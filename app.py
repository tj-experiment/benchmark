import dash
from dash import dcc
from dash import html

import plotly.graph_objects as go

app = dash.Dash(__name__)

languages = [
    'c', 'cpp', 'cython', 'elixir', 'golang', 'node', 'pypy3', 'pypy2',
    'python', 'ruby', 'rust',
]

fig = go.Figure()


for language in languages:
    values = [
        float(i.strip("/\n"))
        for i in open(f"./{language}/output.txt", "r").readlines()
    ]
    fig.add_trace(
        go.Bar(
            y=values,
            name=language,
        ),
    )

# Change the bar mode
fig.update_layout(
    title='10_000_000 iterations',
    xaxis_title="Language",
    yaxis_title="time in seconds",
    legend_title="Language",
    barmode='group',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)

app.layout = html.Div(children=[
    html.H1(children='Speed Test'),
    dcc.Graph(
        id='speed-graph',
        figure=fig,
        style={
            'width': '100%',
            'height': '40rem',
        },
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)