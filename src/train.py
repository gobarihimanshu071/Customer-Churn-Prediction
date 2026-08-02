import pandas as pd
import joblib
import os
from preprocess import (
    clean_data,
    split_features_target,
    encode_features,
    split_data,
    scale_features,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    return df

def train_model(X_train,y_train):
    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test,predictions)
    print(f"\nAccuracy: {accuracy:.4f}\n")

    print("Classification Report")
    print(classification_report(y_test,predictions))

    print("Confusion Matrix")
    print(confusion_matrix(y_test,predictions))
    

def save_model(model,scaler,feature_columns):
    os.makedirs("model",exist_ok=True)

    joblib.dump(model,"model/churn_model.pkl")

    joblib.dump(scaler,"model/scaler.pkl")

    joblib.dump(
        feature_columns,
        "model/feature_columns.pkl"
    )
    print("\nmodel saved successfully!")
    

def main():
    df = load_data("data/Telco-Customer-Churn.csv")

    df = load_data("data/Telco-Customer-Churn.csv")

    df = clean_data(df)

    X, y = split_features_target(df)

    X = encode_features(X)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train_scaled, X_test_scaled, scaler = scale_features(
        X_train,
        X_test,
)

    print("Preprocessing completed successfully!")
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")

    model = train_model(X_train_scaled,y_train)
    evaluate_model(
        model,X_test_scaled,
        y_test
    )

    save_model(
        model,
        scaler,
        X_train.columns.tolist()
    )

if __name__ == "__main__":
    main()
    