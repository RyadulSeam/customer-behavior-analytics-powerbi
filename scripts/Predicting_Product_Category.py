import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# ✅ Dataset path
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw_data")
file_path = os.path.abspath(os.path.join(BASE_DIR, "customer_shopping_behavior.csv"))

df = pd.read_csv(file_path)

# ✅ Encode categorical target
le_category = LabelEncoder()
df['category_encoded'] = le_category.fit_transform(df['Category'])

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

# 🔹 Feature selection (use correct column names)
features = ['Purchase Amount (USD)', 'Age', 'purchase_frequency_days', 'Review Rating']
X = df[features]
y = df['category_encoded']

# 🔹 Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 🔹 Predictions and evaluation
y_pred = clf.predict(X_test)
print("\n✅ Classification Report:\n")
print(classification_report(y_test, y_pred))
