import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import Dataset
df = pd.read_csv("F:\customer-behavior-analytics-powerbi\data\raw_data\customer_shopping_behavior.csv")

# Basic exploration
print(df.head(10))
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe(include="all"))

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# Missing values
print(df.isnull().sum())

# Visualize missing data
sns.heatmap(df[['review_rating']].isnull(), cbar=False, cmap='coolwarm')
plt.show()

# Fill missing values
df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
