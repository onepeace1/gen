from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Database URL
DATABASE_URL = "postgresql://postgres:0000@localhost:5432/postgres"  # Update this with your actual connection string
# Create a engine
engine = create_engine(DATABASE_URL)
# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Creat
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
