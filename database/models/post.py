from ..database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from .history import history   

class post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    selftext = Column(String)
    sentiment = Column(String)
    history_id = Column(Integer, ForeignKey('history.id'))
