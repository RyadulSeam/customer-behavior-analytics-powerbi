import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("F:\customer-behavior-analytics-powerbi\data\raw_data\customer_shopping_behavior.csv")

# Encode categorical features
le_category = LabelEncoder()
df['category_encoded'] = le_category.fit_transform(df['category'])

X = df[['purchase_amount','age','purchase_frequency_days','review_rating']]
y = df['category_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
