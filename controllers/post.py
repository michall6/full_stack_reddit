from uuid import UUID
from services.analyze_sentiment import AnalyzingSentimentService
from services.reddit import RedditService
from database.models import post as post_models
from sqlalchemy.orm import Session
from controllers.history import HistoryCtrl

class RedditCtrl:
 @staticmethod
 async def get_post_details(data:dict,search_id):
     try:
            posts = []
            for post_data in data['data']['children']:
                post = {
                    'id': post_data['data']['id'],
                    'title': post_data['data']['title'],
                    'selftext': post_data['data']['selftext'],
                    'sentiment': AnalyzingSentimentService.analyze_sentiment(str(post['data']['title'])),
                    'search_id':  search_id
                }
                post_instance = post(**post) 
                posts.append(post_instance)
                return posts 
     except Exception as e:
      print("/error in post_details", e)
@staticmethod
async def get_posts(data:dict,search_id:UUID):
     try:
            posts = []
            for post_data in data['data']['children']:
                post = RedditCtrl.get_post_details(post_data,search_id)
                post_instance = post(**post) 
                posts.append(post_instance)
                return posts 
     except Exception as e:
      print("/error in post_details", e)
@staticmethod
async def save_posts(posts: list, db:Session):
        try:
            for post in posts:
                post_to_save = post_models.post(**post)
                db.add(post_to_save)
                db.commit()
                db.refresh(post_to_save)
        except Exception as e:
            print("error in save_posts", e)
@staticmethod
async def search_posts(subreddit:str, category:str, db:Session):
        search_id = HistoryCtrl.save_search(subreddit, category, db)
        data = RedditService.fetch_posts(subreddit, category)
        posts =RedditCtrl.get_posts(data,search_id)
        RedditCtrl.save_posts(posts, db)
        return posts




        