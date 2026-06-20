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