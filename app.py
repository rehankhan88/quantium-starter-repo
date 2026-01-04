#!/usr/bin/env python3
from pink_morsels import create_app
import pandas as pd
import dash
import plotly.express as px


from dash import dcc, html, Input, Output


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



# -------------------------
# Load data
# -------------------------
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# -------------------------
# Dash app
# -------------------------
app = dash.Dash(__name__)
app.title = "Pink Morsels Sales"

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsels Sales Visualiser", className="title"),

        html.Div(
            className="controls",
            children=[
                html.Label("Select Region:", className="label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                ),
            ],
        ),

        dcc.Graph(id="sales-chart"),
    ],
)

# -------------------------
# Callback
# -------------------------
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered_df = df[df["product"] == "Pink Morsels"]

    if region != "all":
        filtered_df = filtered_df[filtered_df["region"] == region]

    filtered_df = filtered_df.sort_values("date")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        labels={
            "date": "Date",
            "sales": "Sales"
        },
        title="Pink Morsels Sales Over Time"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase",
        annotation_position="top left"
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)

