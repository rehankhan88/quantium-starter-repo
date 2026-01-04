#!/usr/bin/env python3
from pink_morsels import create_app
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


# Load processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Filter Pink Morsels only
pink_df = df[df["product"] == "Pink Morsels"].sort_values("date")

# Line chart
fig = px.line(
    pink_df,
    x="date",
    y="sales",
    labels={
        "date": "Date",
        "sales": "Sales"
    },
    title="Pink Morsels Sales Over Time"
)

# Mark price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    annotation_text="Price Increase",
    annotation_position="top left"
)

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsels Sales Visualiser"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
