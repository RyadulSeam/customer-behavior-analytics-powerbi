import pandas as pd
import numpy as np

df = pd.read_csv("F:\customer-behavior-analytics-powerbi\data\raw_data\customer_shopping_behavior.csv")

# Age group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

# Purchase frequency mapping
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# Feature engineering
df['total_amount'] = df['purchase_amount']
df['basket_size'] = df['previous_purchases'] + 1
df['price_category'] = pd.cut(df['purchase_amount'], bins=[0, 30, 60, 100], labels=['Low', 'Medium', 'High'])
df['loyalty_score'] = np.where(df['subscription_status'] == 'Yes', 1, 0) + \
                      np.where(df['purchase_frequency_days'] <= 30, 1, 0)

print(df.head())
