from fastapi import FastAPI
from sqlalchemy.orm import Session

from api.schemas import Customer
from api.database import SessionLocal
from api.models import Prediction
from src.predict import predict_churn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0",
    description="""
    REST API for predicting telecom customer churn using a Logistic Regression Pipeline.
    """
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    print(customer.model_dump())
    result = predict_churn(customer.model_dump())

    db = SessionLocal()

    prediction = Prediction(
        gender=customer.gender,
        senior_citizen=customer.SeniorCitizen,
        partner=customer.Partner,
        dependents=customer.Dependents,
        tenure=customer.tenure,
        phone_service=customer.PhoneService,
        multiple_lines=customer.MultipleLines,
        internet_service=customer.InternetService,
        online_security=customer.OnlineSecurity,
        online_backup=customer.OnlineBackup,
        device_protection=customer.DeviceProtection,
        tech_support=customer.TechSupport,
        streaming_tv=customer.StreamingTV,
        streaming_movies=customer.StreamingMovies,
        contract=customer.Contract,
        paperless_billing=customer.PaperlessBilling,
        payment_method=customer.PaymentMethod,
        monthly_charges=customer.MonthlyCharges,
        total_charges=customer.TotalCharges,
        prediction=result["prediction"],
        churn_probability=result["churn_probability"]
    )

    db.add(prediction)
    db.commit()
    db.close()

    return result

from fastapi.encoders import jsonable_encoder

@app.get("/predictions")
def get_predictions():

    db = SessionLocal()

    predictions = (
        db.query(Prediction)
        .order_by(Prediction.id.desc())
        .limit(10)
        .all()
    )

    return jsonable_encoder(predictions)