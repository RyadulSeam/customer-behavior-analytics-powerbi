import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2

# ✅ Load environment variables
load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# ✅ Import Dataset 
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data")
file_path = os.path.abspath(os.path.join(BASE_DIR, "customer_shopping_behavior.csv"))
df = pd.read_csv(file_path)

# ✅ Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^\w]", "", regex=True)
)

# ✅ Rename column
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

# ✅ Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# ✅ Test psycopg2 connection
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

# ✅ Upload to PostgreSQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")

