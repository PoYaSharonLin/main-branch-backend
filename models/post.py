from sqlalchemy import Column, String, Text, BigInteger, DateTime, event
from database import Base
from datetime import datetime, timedelta

def now():
    return datetime.now()+timedelta(hours=8)

class Post(Base):
    __tablename__ = "posts"
    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String(length=100), index=True)
    content = Column(Text)
    poster = Column(BigInteger)
    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now(), onupdate=now())