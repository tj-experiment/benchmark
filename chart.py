import plotly.graph_objects as go
import numpy as np

languages = [
    'c', 'cpp', 'cython', 'elixir', 'golang', 'node', 'python', 'ruby', 'rust',
]

values = {
    language: [
        float(i.strip("/\n"))
        for i in open(f"./{language}/output.txt", "r").readlines()
    ]
    for language in languages
}

fig = go.Figure()


for language in languages:
    fig.add_trace(
        go.Bar(
            y=values[language],
            name=language,
        ),
    )

# Change the bar mode
fig.update_layout(
    title='10_000_000 iterations',
    xaxis_title="Language",
    yaxis_title="time in milliseconds",
    legend_title="Language",
    barmode='group',
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)
fig.show()
