from databaseControllers.history import HistoryDBCtrl
from database.database import db
from database.models.post import post as post_models


class RedditDBCtrl:
 @staticmethod
 def save_posts(posts: list):
        try:
            for post in posts:
                post_to_save = post_models(**post)
                db.add(post_to_save)
                db.commit()
            db.refresh(post_to_save)
        except Exception as e:
            print("error in save_posts", e)

 
 







        