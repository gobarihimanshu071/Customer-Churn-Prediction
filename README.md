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

## Exploratory Data Analysis

### Churn Distribution
- 73.46% retained customers
- 26.54% churned customers

### Key Findings

#### Tenure
- Churned customers had average tenure of 17.98 months.
- Retained customers had average tenure of 37.57 months.

#### Monthly Charges
- Churned customers paid higher monthly charges on average.
- Mean MonthlyCharges:
  - Churned: 74.44
  - Retained: 61.27

#### Contract Type
- Month-to-month: 42.71% churn rate
- One year: 11.27% churn rate
- Two year: 2.83% churn rate

#### Online Security
- No Online Security: 41.77% churn rate
- Online Security: 14.61% churn rate

#### Tech Support
- No Tech Support: 41.64% churn rate
- Tech Support: 15.17% churn rate

### Preliminary Churn Drivers
1. Contract Type
2. Tenure
3. Online Security
4. Tech Support
5. Monthly Charges

#### Internet Service

Churn Rate by Internet Service:

- Fiber Optic: 41.89%
- DSL: 18.96%
- No Internet Service: 7.40%

Business Insight:

Fiber Optic customers exhibited significantly higher churn rates than DSL customers. This may indicate higher pricing sensitivity, greater customer expectations, or interactions with other service-related features.