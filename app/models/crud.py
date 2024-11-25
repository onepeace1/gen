from sqlalchemy.orm import Session
from app.models import models

def create_news_batch(db: Session, news_list: list):
    db.add_all(news_list)
    db.commit()
    db.refresh(news_list)
    return news_list

#DB에 추가
def add_news(db: Session, news_data: dict):
    db_news = models.News(**news_data)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news
