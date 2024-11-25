from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import models, crud, database, schemas
from .services.Summarize import summarize 
import pytz
from datetime import datetime, timedelta
from .models.database import get_db


app = FastAPI()


@app.post("/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):
    db_news = crud.create_news(db=db, news=news)
    return db_news


# DB 세션 열기
db = database.SessionLocal()


db.close()
