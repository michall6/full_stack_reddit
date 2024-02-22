from fastapi import HTTPException
import requests
from services.auth import auth_headers


class RedditService:
    
    @staticmethod
    def  posts_from_reddit(subreddit, category):
        
        url = f'https://oauth.reddit.com/r/{subreddit}/{category}?limit=9'
        try:
            res = requests.get(url, headers=auth_headers())
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
       
        return res.json()['data']['children']


