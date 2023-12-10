import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 1, 3]
}

df = pd.DataFrame(data)

# Create Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(children=[
    html.H1("Simple Dash App with Bar Chart"),
    
    dcc.Graph(
        id='simple-bar-chart',
        figure=px.bar(df, x='Category', y='Value', title='Simple Bar Chart')
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)
