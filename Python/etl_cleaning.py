
import pandas as pd

# Load CSV
df = pd.read_csv("../data/liquor_sales.csv")

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert date column
df["sale_date"] = pd.to_datetime(df["sale_date"])

# Remove rows with missing sales
df = df[df["sale_dollars"].notnull()]

# Add calculated column
df["avg_bottle_price"] = df["sale_dollars"] / df["bottles_sold"]

# Save cleaned file
df.to_csv("../data/liquor_sales_cleaned.csv", index=False)

print("ETL complete. Cleaned file saved.")