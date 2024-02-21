from fastapi import APIRouter
from database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from controllers.post import RedditCtrl

router = APIRouter()

@router.get("/{subreddit}/{category}")
async def get_posts(subreddit:str, category:str, db:Session = Depends(get_db)):  
    try:  
        return await RedditCtrl.search_posts(subreddit, category, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")