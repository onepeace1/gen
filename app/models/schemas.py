from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NewsBase(BaseModel):
    news_data : datetime
    news_ranking: int
    category: str
    url: str
    img_url: Optional[str] = None
    title: str
    content_summarize: str
    content: str

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int
    news_date: str  # datetime을 str로 변환

    class Config:
        orm_mode = True
