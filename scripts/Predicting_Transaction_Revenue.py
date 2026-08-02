import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# ✅ Dataset path
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data")
file_path = os.path.abspath(os.path.join(BASE_DIR, "customer_shopping_behavior.csv"))

df = pd.read_csv(file_path)

# 🔹 Map purchase frequency into numeric days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['Frequency of Purchases'].map(frequency_mapping)

# ✅ Features and target
X = df[['Age', 'purchase_frequency_days', 'Review Rating']]
y = df['Purchase Amount (USD)']

# 🔹 Handle missing values (median imputation)
imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(X)

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42),
    "HistGradientBoosting": HistGradientBoostingRegressor(random_state=42)
}

results = {}
predictions = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    results[name] = rmse
    predictions[name] = y_pred
    print(f"{name} RMSE: {rmse:.2f}")

# ✅ Plot results
plt.bar(results.keys(), results.values(), color=['skyblue','lightgreen','salmon','orange'])
plt.ylabel("RMSE")
plt.title("Model Comparison")
plt.show()
