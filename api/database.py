from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "mysql+pymysql://admin:Theforeverstory2022@"
    "churn-db.c9ageogoy5iq.us-east-2.rds.amazonaws.com:3306/customer_churn"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

from api.database import engine
from api.models import Base

Base.metadata.create_all(bind=engine)