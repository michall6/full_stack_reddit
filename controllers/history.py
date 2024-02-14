from sqlalchemy.orm import Session
from database.models import history as models

class HistoryCtrl:
    @staticmethod
    def save_search(subreddit:str, category:str, db:Session):
        try:
            search_details = models.history(
                subreddit=subreddit,
                category=category
            )
            db.add(search_details)
            db.commit()
            db.refresh(search_details)
            
            search_id = db.query(models.history.id).order_by(models.history.id.desc()).first()[0]

            return search_id 
            
        except Exception as e:
            print("/error in save_search", e)