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




