import joblib
import pandas as pd

pipeline = joblib.load("model/churn_pipeline.pkl")

def predict_churn(customer):
    customer_df = pd.DataFrame([customer])

    prediction = pipeline.predict(customer_df)[0]

    probability = pipeline.predict_proba(customer_df)[0]

    churn_probability = probability[
        list(pipeline.classes_).index("Yes")
    ]

    return {
        "prediction": prediction,
        "churn_probability": round(float(churn_probability), 4)
    }




if __name__ == "__main__":

    sample_customer = {

        "gender": "Female",

        "SeniorCitizen": 0,

        "Partner": "No",

        "Dependents": "No",

        "tenure": 2,

        "PhoneService": "Yes",

        "MultipleLines": "No",

        "InternetService": "Fiber optic",

        "OnlineSecurity": "No",

        "OnlineBackup": "No",

        "DeviceProtection": "No",

        "TechSupport": "No",

        "StreamingTV": "No",

        "StreamingMovies": "No",

        "Contract": "Month-to-month",

        "PaperlessBilling": "Yes",

        "PaymentMethod": "Electronic check",

        "MonthlyCharges": 75,

        "TotalCharges": 150
    }

    result = predict_churn(sample_customer)

    print(result)