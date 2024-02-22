from fastapi import HTTPException
from starlette import status
from databaseControllers.history import HistoryDBCtrl
from fastapi import APIRouter

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
def  get_all_searches():
    try:
       return  HistoryDBCtrl.get_all_searches() 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@router.get('/by-id/{id}', status_code=status.HTTP_200_OK)

def get_search_by_id(id:int):
    try:      
        results= HistoryDBCtrl.get_search_by_id(id)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    