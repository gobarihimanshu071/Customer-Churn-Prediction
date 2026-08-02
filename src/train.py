import joblib
import os
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

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

    random_state=42
)

numerical_features = [
    "SeniorCitizen",

    "tenure",

    "MonthlyCharges",

    "TotalCharges"
]

categorical_features = X.select_dtypes(
    include="object"
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
            "classifier",
            LogisticRegression(
                random_state=42,
                max_iter=1000
            )
        )
    ]
)
pipeline.fit(
    X_train,y_train
)

predictions = pipeline.predict(
    X_test
)

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

joblib.dump(pipeline,"model/churn_pipeline.pkl")