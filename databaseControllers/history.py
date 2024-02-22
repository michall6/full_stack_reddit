from database.database import db
from database.models.history import history as history_model
from database.models.post import post as post_model


class HistoryDBCtrl:
  @staticmethod
  def get_all_searches():
        return db.query(history_model).all()
         
  @staticmethod
  def get_search_by_id():
        return db.query(post_model).filter(post_model.history_id==id).all()
         
  @staticmethod
  def  save_search_subreddit_category(subreddit:str, category:str):
        try:
            search_details = history_model(
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


 