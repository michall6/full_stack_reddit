from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    title: str
    content: str
    sentiment: str
    history_id: int
    
    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True