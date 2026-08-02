import joblib
import os
import pandas as pd

from sklearn.compose import ColumnTransformer
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import StratifiedKFold, cross_validate

from sklearn.model_selection import GridSearchCV

df = pd.read_csv("data/Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"]=df["TotalCharges"].fillna(0)

X=df.drop(
    ["customerID","Churn"],
    axis=1
)

y=df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,
    stratify=y
)

numerical_features = [
    "SeniorCitizen",

    "tenure",

    "MonthlyCharges",

    "TotalCharges"
]

categorical_features = X.select_dtypes(
    include=["object","string"]
).columns.tolist()


preprocessor = ColumnTransformer(
    transformers = [
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(
                drop="first",
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ]
)

pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "smote",SMOTE(random_state=42)
        ),
        (
            "classifier",
            LogisticRegression(
                random_state=42,
                max_iter=1000
            )
        )
    ]
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_validate(
    pipeline,
    X,
    y,
    cv=cv,
    scoring=[
        "accuracy",
        "precision_macro",
        "recall_macro",
        "f1_macro"
    ]
)

print("\n===== Cross Validation =====")
print("Accuracy :", scores["test_accuracy"].mean())
print("Precision:", scores["test_precision_macro"].mean())
print("Recall   :", scores["test_recall_macro"].mean())
print("F1 Score :", scores["test_f1_macro"].mean())

param_grid = {
    "classifier__C": [0.01, 0.1, 1, 10],
    "classifier__solver": ["liblinear", "lbfgs"]
}
from sklearn.metrics import make_scorer, recall_score

recall_scorer = make_scorer(
    recall_score,
    pos_label="Yes"
)

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring=recall_scorer,
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\n===== Best Parameters =====")
print(grid_search.best_params_)

print("\n===== Best Recall =====")
print(grid_search.best_score_)

best_pipeline = grid_search.best_estimator_

predictions = best_pipeline.predict(X_test)

y_prob = best_pipeline.predict_proba(X_test)[:, 1]

import numpy as np
from sklearn.metrics import classification_report

thresholds = np.arange(0.1, 0.9, 0.05)

for threshold in thresholds:
    y_pred = np.where(y_prob >= threshold, "Yes", "No")

    print(f"\nThreshold: {threshold:.2f}")
    print(classification_report(y_test, y_pred))

print(
    accuracy_score(
        y_test,
        predictions
    )
)

print(
    classification_report(
        y_test,
        predictions
    )
)

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

os.makedirs("model",exist_ok=True)

joblib.dump(best_pipeline,"model/churn_pipeline.pkl")
print("\nPipeline saved successfully!")