# Customer Churn Prediction

## Objective

Predict whether a customer will leave a telecom company using machine learning.

## Dataset

Telco Customer Churn Dataset

## Project Status

- [x] Project Setup
- [ ] EDA
- [ ] Data Cleaning
- [ ] Feature Engineering
- [ ] Model Training
- [ ] Evaluation
- [ ] Deployment

## Progress

### Dataset Overview

- Records: 7043
- Features: 21
- Target Variable: Churn

## Dataset Inspection

### Shape
- Rows: 7043
- Columns: 21

### Data Types
- Numerical Features: 3
- Categorical Features: 18

### Observation
- `TotalCharges` is stored as object instead of numeric and requires investigation.

### Target Distribution

- Churned Customers: 26.54%
- Retained Customers: 73.46%

### Observation

Dataset exhibits moderate class imbalance and may require techniques such as SMOTE during model training.

### Data Quality Investigation

- `TotalCharges` was stored as object instead of numeric.
- Investigation revealed 11 invalid entries.
- These entries could not be converted to numeric values and require cleaning.

### Data Cleaning

#### TotalCharges

Issue:
- Column stored as object instead of numeric.
- 11 rows contained blank values.

Investigation:
- All affected customers had tenure = 0.

Resolution:
- Replaced blank values with 0.
- Converted TotalCharges to float64.

### Summary Statistics

#### Tenure
- Average tenure: 32.37 months
- Median tenure: 29 months
- Range: 0–72 months

#### Monthly Charges
- Average monthly charge: 64.76
- Range: 18.25–118.75

#### Total Charges
- Average total charge: 2279.73
- Maximum total charge: 8684.80

### Initial Observations
- Large variation exists in customer spending.
- Tenure may be an important predictor of churn.

### Tenure and Churn Analysis

Key Findings:

- Customers who stayed had an average tenure of 37.57 months.
- Customers who churned had an average tenure of 17.98 months.
- Median tenure for churned customers was only 10 months.

Business Insight:

Customer churn is significantly higher among newer customers. Early customer retention programs could substantially reduce churn rates.
# Exploratory Data Analysis (EDA)

## Dataset Overview

- Records: 7043
- Features: 21
- Target Variable: Churn

---

## Data Cleaning

### TotalCharges

- Found 11 blank values in the `TotalCharges` column.
- All affected customers had `tenure = 0`.
- Replaced blank values with `0`.
- Converted `TotalCharges` from object to float.

---

## Target Distribution

| Churn | Percentage |
|--------|------------|
| No | 73.46% |
| Yes | 26.54% |

Observation:

- The dataset has moderate class imbalance.
- This will be handled later using SMOTE.

---

# Key Business Insights

## Tenure

- Customers who churned had an average tenure of **17.98 months**.
- Customers who stayed had an average tenure of **37.57 months**.

**Business Insight**

New customers are much more likely to churn than long-term customers.

---

## Monthly Charges

- Churned customers paid higher monthly charges on average.

| Churn | Mean Monthly Charges |
|--------|----------------------|
| No | 61.27 |
| Yes | 74.44 |

**Business Insight**

Customers paying higher monthly charges are more likely to switch providers.

---

## Contract Type

| Contract | Churn Rate |
|-----------|-----------:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

**Business Insight**

Month-to-month customers have the highest churn.
Long-term contracts significantly improve retention.

---

## Internet Service

| Service | Churn Rate |
|----------|-----------:|
| DSL | 18.96% |
| Fiber Optic | 41.89% |
| No Internet | 7.40% |

**Business Insight**

Fiber Optic customers exhibit significantly higher churn and should be prioritized for retention campaigns.

---

## Online Security

| Security | Churn Rate |
|-----------|-----------:|
| No | 41.77% |
| Yes | 14.61% |
| No Internet Service | 7.40% |

**Business Insight**

Customers without Online Security are almost three times more likely to churn.

---

## Tech Support

| Tech Support | Churn Rate |
|--------------|-----------:|
| No | 41.64% |
| Yes | 15.17% |
| No Internet Service | 7.40% |

**Business Insight**

Providing technical support is strongly associated with lower churn.

---

## Payment Method

| Payment Method | Churn Rate |
|----------------|-----------:|
| Electronic Check | 45.29% |
| Mailed Check | 19.11% |
| Bank Transfer (Automatic) | 16.71% |
| Credit Card (Automatic) | 15.24% |

**Business Insight**

Customers using Electronic Check have the highest churn rate.

---

## Dependents

| Dependents | Churn Rate |
|------------|-----------:|
| No | 31.28% |
| Yes | 15.45% |

**Business Insight**

Customers with dependents are approximately twice as likely to stay compared to customers without dependents.

---

# Overall EDA Summary

The exploratory analysis identified several strong churn indicators:

- Low customer tenure
- Month-to-month contracts
- Fiber Optic internet service
- Lack of Online Security
- Lack of Tech Support
- Electronic Check payment method
- Higher Monthly Charges
- Customers without dependents

These insights will guide feature engineering and help interpret the machine learning models developed in the next phase.



