import pandas as pd
from pathlib import Path

# Path to data folder
data_path = Path("data")

# Read all CSV files
files = list(data_path.glob("*.csv"))

df_list = []
for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all files
data = pd.concat(df_list, ignore_index=True)

# Keep only Pink Morsels
data = data[data["product"] == "Pink Morsels"]

# Create Sales column
data["Sales"] = data["quantity"] * data["price"]

# Keep required columns
final_data = data[["Sales", "date", "region"]]

# Rename columns
final_data.columns = ["Sales", "Date", "Region"]

# Save output file
final_data.to_csv("formatted_sales_data.csv", index=False)

print("Data processing complete.")
