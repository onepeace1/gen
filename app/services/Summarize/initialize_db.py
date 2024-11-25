from datetime import datetime, timedelta
import pytz
from app.services.Summarize import summarize
from app.models import models
from app.models.database import get_db
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

# 초기 데이터 (2024년 data)
def initialize_database(db: Session):
    t = timedelta(days=1)
    seoul_tz = pytz.timezone('Asia/Seoul')
    initial_news = []
    
    try:
        for i in range(1, 3):
            news_date = (datetime.now(seoul_tz)-t*i).replace(minute=0, second=0, microsecond=0)
            
            # 해당 날짜의 데이터가 이미 존재하는지 확인
            existing_news = db.query(models.News).filter(
                models.News.news_date == news_date
            ).first()
            
            if not existing_news:
                news = summarize.initial_data(news_date)  #비동기함수로 변경하는 선택지도
                for j in news:
                    initial_news.append(models.News(
                        news_date=j[0],
                        news_ranking=j[1],
                        category=j[7],
                        url=j[2],
                        img_url=j[3],
                        title=j[4],
                        content_summarize=j[6],
                        content=j[5]
                    ))
                
                # 일정 크기마다 벌크 저장 (메모리 관리)
                if len(initial_news) >= 10:
                    db.add_all(initial_news)
                    db.commit()
                    initial_news = []
        
        # 남은 데이터 저장
        if initial_news:
            db.add_all(initial_news)
            db.commit()
            
    except Exception as e:
        db.rollback()
        raise Exception(f"데이터베이스 초기화 중 오류 발생: {str(e)}")

def init_db(db: Session = Depends(get_db)):
    try:
        initialize_database(db)
        return {"message": "데이터베이스 초기화 완료"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 실행 코드 수정
if __name__ == "__main__":  # 직접실행할 때만 실행되는 코드
    import asyncio
    from app.models.database import SessionLocal
    
    # 비동기 실행을 위한 메인 함수
    def main():
        db = SessionLocal()
        try:
            init_db(db)
        finally:
            db.close()
    
    # 비동기 함수 실행
    main()
