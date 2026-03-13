import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("../data/liquor_sales_cleaned.csv")

# PostgreSQL connection
engine = create_engine("postgresql://postgres:yourpassword@localhost:5432/liquor_db")

# Load into SQL table
df.to_sql("liquor_sales", engine, if_exists="append", index=False)

print("Data loaded into PostgreSQL successfully.")