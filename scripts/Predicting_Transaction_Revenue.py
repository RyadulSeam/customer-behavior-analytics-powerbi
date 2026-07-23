import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("F:\customer-behavior-analytics-powerbi\data\raw_data\customer_shopping_behavior.csv")

X = df[['age','purchase_frequency_days','review_rating']]
y = df['purchase_amount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    results[name] = rmse
    print(f"{name} RMSE: {rmse:.2f}")

# Plot results
plt.bar(results.keys(), results.values(), color=['skyblue','lightgreen','salmon'])
plt.ylabel("RMSE")
plt.title("Model Comparison")
plt.show()

# Save predictions
df_results = pd.DataFrame({"y_test": y_test, "y_pred": y_pred})
df_results.to_csv("predictions.csv", index=False)
