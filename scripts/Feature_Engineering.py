import os
import pandas as pd
import numpy as np

# Define base directory relative to scripts folder
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data")
file_path = os.path.abspath(os.path.join(BASE_DIR, "customer_shopping_behavior.csv"))

# Load dataset
df = pd.read_csv(file_path)

# Check columns
print("Available columns:", df.columns)

# 🔹 Age group segmentation (only if 'Age' column exists)
if 'Age' in df.columns:
    age_labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
    df['age_group'] = pd.qcut(df['Age'], q=4, labels=age_labels)

# 🔹 Purchase frequency mapping
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
if 'frequency_of_purchases' in df.columns:
    df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# 🔹 Feature engineering
if 'purchase_amount' in df.columns:
    df['total_amount'] = df['purchase_amount']
if 'previous_purchases' in df.columns:
    df['basket_size'] = df['previous_purchases'] + 1
if 'purchase_amount' in df.columns:
    df['price_category'] = pd.cut(
        df['purchase_amount'],
        bins=[0, 30, 60, 100],
        labels=['Low', 'Medium', 'High']
    )
if 'subscription_status' in df.columns and 'purchase_frequency_days' in df.columns:
    df['loyalty_score'] = (
        np.where(df['subscription_status'] == 'Yes', 1, 0) +
        np.where(df['purchase_frequency_days'] <= 30, 1, 0)
    )

# Preview transformed dataset
print(df.head())
