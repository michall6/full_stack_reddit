from sqlalchemy.orm import Session
from database.models import history as history_model

class HistoryCtrl:
    @staticmethod
    def save_search_subreddit_category(subreddit:str, category:str, db:Session):
        try:
           
            search_details = history_model.history(
                subreddit=subreddit,
                category=category
            )
            db.add(search_details)
            db.commit()
            db.refresh(search_details)
            
            search_id = db.query(history_model.history.id).order_by(history_model.history.id.desc()).first()[0]

            return search_id 
            
        except Exception as e:
            print("/error in save_search_subreddit_category", e)


 