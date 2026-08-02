from fastapi import FastAPI
from sqlalchemy.orm import Session

from api.schemas import Customer
from api.database import SessionLocal
from api.models import Prediction
from src.predict import predict_churn

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    description="""
    REST API for predicting telecom customer churn using a Logistic Regression Pipeline.
    """
)

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }

@app.post(
    "/predict",
    summary="Predict Customer Churn",
    description="Returns churn prediction and probability."
)
def predict(customer: Customer):

    result = predict_churn(customer.model_dump())

    db: Session = SessionLocal()

    prediction = Prediction(
        **customer.model_dump(),
        prediction=result["prediction"],
        churn_probability=result["churn_probability"]
    )

    db.add(prediction)
    db.commit()
    db.close()

    return result