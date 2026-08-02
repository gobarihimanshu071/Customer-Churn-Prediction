import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    return df

def split_features_target(df):
    X=df.drop(["customerID","Churn"],axis=1)
    y=df["Churn"]

    return X,y

def encode_features(X):
    X=pd.get_dummies(
        X,
        drop_first=True,
        dtype=int
    )

    return X

def split_data(X,y):
    return train_test_split(
        X,y,test_size=0.2,random_state=42
    )

def scale_features(X_train,X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler