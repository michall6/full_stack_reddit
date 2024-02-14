from ..database import Base
from sqlalchemy import Column, Integer, String

class history(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    subreddit = Column(String)
    category = Column(String)