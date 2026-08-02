import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Define base directory relative to scripts folder
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data")
file_path = os.path.abspath(os.path.join(BASE_DIR, "customer_shopping_behavior.csv"))

# ✅ Import Dataset
df = pd.read_csv(file_path)

# 🔹 Basic exploration
print("First 10 rows:\n", df.head(10))
print("Shape:", df.shape)
print("Data types:\n", df.dtypes)
print("Info:\n")
df.info()
print("Summary statistics:\n", df.describe(include="all"))

# 🔹 Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

# 🔹 Missing values check
print("Missing values:\n", df.isnull().sum())

# 🔹 Visualize missing data
sns.heatmap(df[['review_rating']].isnull(), cbar=False, cmap='coolwarm')
plt.title("Missing Review Ratings")
plt.show()

# 🔹 Fill missing values by category median
df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))

print("Missing values after filling:\n", df.isnull().sum())
