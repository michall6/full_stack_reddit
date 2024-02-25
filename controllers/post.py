from uuid import UUID
from databaseControllers.history import HistoryDBCtrl
from databaseControllers.post import RedditDBCtrl
from services.RedditService import RedditService
from services.analyze_sentiment import AnalyzingSentimentService

class RedditCtrl:
 @staticmethod
 def get_posts(posts:dict,search_id:UUID):
     try:
         get_post_details = [RedditCtrl.get_post_details(post, search_id) for post in posts]
         return get_post_details     
                
     except Exception as e:
      print("/error in controllers get_posts", e)

 @staticmethod
 def search_posts(subreddit:str, category:str):
        search_id =  HistoryDBCtrl.save_search_subreddit_category(subreddit, category)
        data =  RedditService.posts_from_reddit(subreddit, category)
        posts =  RedditCtrl.get_posts(data,search_id)
        RedditDBCtrl.save_posts(posts)
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
      print("/error in controllers post_details hhhhh", e)





        