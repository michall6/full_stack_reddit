from pydantic import BaseModel

class HistoryBase(BaseModel):
    id: int
    subreddit: str
    category: str

    
    class Config:
        orm_mode = True

class CreateHistory(HistoryBase):
    class Config:
        orm_mode = True