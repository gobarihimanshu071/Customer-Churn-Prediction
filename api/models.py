from sqlalchemy import Column, Integer, String, Boolean, DECIMAL, TIMESTAMP
from sqlalchemy.sql import func
from api.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    gender = Column(String(10))
    senior_citizen = Column(Boolean)
    partner = Column(Boolean)
    dependents = Column(Boolean)

    tenure = Column(Integer)

    phone_service = Column(Boolean)
    multiple_lines = Column(String(30))

    internet_service = Column(String(30))
    online_security = Column(String(30))
    online_backup = Column(String(30))
    device_protection = Column(String(30))
    tech_support = Column(String(30))
    streaming_tv = Column(String(30))
    streaming_movies = Column(String(30))

    contract = Column(String(30))
    paperless_billing = Column(Boolean)
    payment_method = Column(String(50))

    monthly_charges = Column(DECIMAL(10,2))
    total_charges = Column(DECIMAL(10,2))

    prediction = Column(String(10))
    churn_probability = Column(DECIMAL(5,4))

    created_at = Column(TIMESTAMP, server_default=func.now())