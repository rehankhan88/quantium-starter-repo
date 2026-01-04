from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import os

# -------------------------
# Load CSV if it exists, otherwise use sample data
# -------------------------
CSV_PATH = "formatted_sales_data.csv"

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    # Ensure correct columns exist
    required_cols = {"date", "region", "sales", "product"}
    if required_cols.issubset(df.columns):
        df["date"] = pd.to_datetime(df["date"])
        df = df[df["product"] == "Pink Morsels"]
    else:
        print("CSV missing required columns. Using sample data.")
        df = pd.DataFrame({
            "region": ["North", "South", "East", "West"],
            "sales": [100, 150, 200, 130]
        })
else:
    df = pd.DataFrame({
        "region": ["North", "South", "East", "West"],
        "sales": [100, 150, 200, 130]
    })

# -------------------------
# Initialize Dash app
# -------------------------
app = Dash(__name__)
app.title = "Pink Morsels Sales"

# Create initial figure
fig = px.bar(df, x="region", y="sales", title="Pink Morsels Sales")

# -------------------------
# Layout
# -------------------------
app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser", id="header"),

    html.Label("Select Region:", htmlFor="region-picker"),
    dcc.Dropdown(
        id="region-picker",
        options=[{"label": r, "value": r} for r in df["region"]],
        value=df["region"].iloc[0] if not df.empty else "North"
    ),

    dcc.Graph(id="sales-graph", figure=fig)
])

# -------------------------
# Callback
# -------------------------
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):
    filtered_df = df[df["region"] == selected_region] if not df.empty else df
    fig = px.bar(filtered_df, x="region", y="sales", title="Pink Morsels Sales")
    return fig

# -------------------------
# Run server
# -------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
