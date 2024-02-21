from uuid import UUID
from services.analyze_sentiment import AnalyzingSentimentService
from services.reddit import RedditService
from database.models.post import post as post_models
from sqlalchemy.orm import Session
from controllers.history import HistoryCtrl

class RedditCtrl:
 @staticmethod
 def save_posts(posts: list, db:Session):
        try:
            for post in posts:
                post_to_save = post_models(**post)
                db.add(post_to_save)
                db.commit()
            db.refresh()
        except Exception as e:
            print("error in save_posts", e)

 @staticmethod
 def get_posts(posts:dict,search_id:UUID):
     try:
         get_post_details = [RedditCtrl.get_post_details(post, search_id) for post in posts]
         return get_post_details     
                
     except Exception as e:
      print("/error in get_posts", e)

 @staticmethod
 async def search_posts(subreddit:str, category:str, db:Session):
        search_id =  HistoryCtrl.save_search_subreddit_category(subreddit, category, db)
        data = await RedditService.posts_from_reddit(subreddit, category)
        posts =  RedditCtrl.get_posts(data,search_id)
        RedditCtrl.save_posts(posts, db)
        return posts
 
 @staticmethod
 def get_post_details(post_data:dict,search_id :UUID):
     try:
                return {
                    
                    'title': post_data['data']['title'],
                    'selftext': post_data['data']['selftext'],
                    'sentiment': AnalyzingSentimentService.analyze_sentiment(str(post_data['data']['title'])),
                    'history_id':  search_id
                }
                   
     except Exception as e:
      print("/error in post_details hhhhh", e)







        