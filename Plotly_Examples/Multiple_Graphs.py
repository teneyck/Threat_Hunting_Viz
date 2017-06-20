import plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5],
    y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
)
trace2 = go.Bar(
    x=[0, 1, 2, 3, 4, 5],
    y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
)

data = [trace1, trace2]
py.offline.plot(data, filename='bar-line')
