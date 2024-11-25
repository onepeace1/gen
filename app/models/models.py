from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, TIMESTAMP
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql import func

# Define the base
Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    news_date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    news_ranking = Column(Integer)
    category = Column(Text)
    url = Column(Text)
    img_url = Column(Text)
    title = Column(Text)
    content_summarize = Column(Text)
    content = Column(Text)
