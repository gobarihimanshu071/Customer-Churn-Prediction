from fastapi import FastAPI

from api.schemas import Customer
from src.predict import predict_churn

app = FastAPI(

    title="Customer Churn Prediction API",

    version="1.0.0",

    description="""
    REST API for predicting telecom customer churn using a Logistic Regression Pipeline.
    """
)

@app.get("/",tags=["Home"])
def home():
    return{
        "message": "Customer Churn Prediction API is running!"
     }

@app.post(
    "/predict",
    summary="Predict Customer Churn",
    description="Returns churn prediction and probability."
)
def predict(customer: Customer):
    result = predict_churn(customer.model_dump())
    return result

