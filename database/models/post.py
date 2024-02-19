from ..database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    selftext = Column(String)
    sentiment = Column(String)
    search_id= Column(Integer, ForeignKey('history.id'))
