# Executive Summary: Customer Behaviour & Predictive Analytics Project

## 1. Project Overview & Performance Highlights
This project provides a comprehensive analysis of customer purchasing behaviour, product performance, and operational logistics. By synthesising data from multiple streams—including demographic profiles, subscription status, and shipping methods—the analysis identifies key revenue drivers and opportunities to optimise market strategy. The scope encompasses the development of predictive models to forecast purchase amounts and categorise product preferences, alongside the creation of business intelligence dashboards to monitor organisational health.

### Key Performance Indicators (KPIs)
| Metric | Value |
| :--- | :--- |
| **Total Revenue** | $233.2K (+5.4% growth) |
| **Total Active Users** | 3,901 |
| **Average Order Value (AOV)** | $59.77 |
| **Average Review Rating** | 3.75 Stars |
| **Net Promoter Score (NPS)** | 41.89 |

---

## 2. Revenue Drivers & Demographic Analysis
The analysis of customer demographics reveals a clear hierarchy in revenue contribution based on age group. The following segments represent the total revenue distribution:

* **Adult:** $90K (The primary driver and highest revenue growth segment)
* **Middle-Aged:** $66K
* **Senior:** $39K
* **Young Adult:** $35K

The dominance of the 'Adult' segment, particularly regarding its superior growth rate, justifies a strategy that prioritises this demographic for future market targeting. By focusing resources on this high-performing tier, the organisation can sustain momentum while investigating engagement strategies for the Middle-Aged and Senior tiers.

### Revenue by Category and Gender
| Category | Revenue by Gender (Female/Male) |
| :--- | :--- |
| **Clothing** | Female: $71K |
| **Accessories** | Female: $50K |

---

## 3. Product Portfolio & Category Performance
Clothing has been identified as the dominant product category, serving as the foundational pillar of total revenue. Within the portfolio, high-value staples demonstrate varying degrees of growth.

### Top 5 Products by Revenue
* **Blouse:** $10.4K (+6.7%)
* **Shirt:** $10.3K (+5.1%)
* **Dress:** $10.3K (+5.2%)
* **Pants:** $10.1K (+8.1%)
* **Jewelry:** $10.0K (-3.1%)

### Seasonal Preferences
Data-driven insights into seasonal demand highlight shifting consumer needs based on order volume. During the Fall season, the Jacket is the highest-performing item, whereas the Sweater becomes the primary item of interest during the Spring.

---

## 4. Subscription Dynamics & Customer Loyalty
The subscription model is a critical driver for the organisation, contributing **73.13% ($170.5K)** of total revenue. However, a notable **26.87% ($62.6K)** is still derived from non-subscribers.

Based on SQL analysis of purchase history, customers are segmented as follows:
* **New:** 1 purchase.
* **Returning:** 2–10 purchases.
* **Loyal:** 10+ purchases.

A strategic comparison of spend profiles reveals that non-subscribers maintain a slightly higher average spend per order despite the lower total volume they contribute to the business. This indicates a high-value opportunity for converting these intermittent shoppers into long-term subscribers.

---

## 5. Logistics & Experience Metrics
Operational performance is tracked across a variety of shipping methods, each impacting revenue and customer perception:
* Free Shipping
* Express
* Store Pickup
* Standard
* 2-Day Shipping
* Next Day Air

The current Net Promoter Score (NPS) stands at **41.89**, which falls significantly below the target benchmark of **70**. This discrepancy signals an urgent requirement for loyalty initiatives. Correlation analysis confirms that shipping methods—specifically the balance between speed and cost—directly influence customer satisfaction ratings.

---

## 6. Predictive Analytics & Data Science Insights
Predictive modelling was employed to enhance forecasting for purchase amounts and product categorisation. Multiple regression models were evaluated to identify the most accurate method for predicting transaction values.

### Model Performance (Regression)
| Model Type | Root Mean Square Error (RMSE) |
| :--- | :--- |
| **Linear Regression** | ~23.5 |
| **XGBoost** | ~26.5 |
| **Random Forest** | ~27.0 |

Linear Regression provided the most accurate predictions with the lowest error rate. Furthermore, classification models were successfully implemented to predict product categories based on specific customer features, enabling more personalised marketing approaches.

---

## 7. Strategic Recommendations

1. **NPS Improvement:** Implementation of immediate loyalty and service-recovery initiatives is essential to bridge the 28.11-point deficit required to meet the 70-point industry benchmark.
2. **Targeted Marketing:** Aggressively focus resource allocation on the 'Adult' demographic and the 'Clothing' category, as these are the proven primary engines of revenue and growth.
3. **Subscription Growth:** Develop specific conversion incentives targeting the 26.87% of revenue currently generated by non-subscribers to secure more predictable, long-term revenue streams.
4. **Logistics Optimisation:** Scrutinise the performance of 'Free Shipping' and 'Express' delivery methods. By leveraging granular data to prioritise the shipping profiles most strongly correlated with high satisfaction, the organisation can improve overall brand perception and review ratings.