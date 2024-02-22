from fastapi import APIRouter
from fastapi import  HTTPException
from controllers.post import RedditCtrl

router = APIRouter()

@router.get("/{subreddit}/{category}")
def get_posts(subreddit:str, category:str):  
    try:  
        return  RedditCtrl.search_posts(subreddit, category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")