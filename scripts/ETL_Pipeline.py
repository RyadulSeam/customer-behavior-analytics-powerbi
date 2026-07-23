import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

# Import Dataset
df = pd.read_csv("F:\customer-behavior-analytics-powerbi\data\raw_data\customer_shopping_behavior.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w]', '', regex=True)

# Rename column
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# Connect to PostgreSQL
username = "postgres"
password = "1234"
host = "localhost"
port = "5432"
database = "Customer_behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

try:
    conn = psycopg2.connect(
        dbname=database,
        user=username,
        password=password,
        host=host,
        port=port
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

# Upload to PostgreSQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
