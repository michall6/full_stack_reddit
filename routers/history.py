from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from database.models.history import history
from database.models import post as post
from fastapi import APIRouter
from database.database import get_db

router = APIRouter()

@router.get('/all', status_code=status.HTTP_200_OK)
def  get_all_searches(db: Session = Depends(get_db)):
    try:
       return   db.query(history).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@router.get('/by-id/{id}', status_code=status.HTTP_200_OK)
def get_search_by_id(id:int, db: Session = Depends(get_db)):
    try:
        results=db.query(post).filter(post.search_id==id).all()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    