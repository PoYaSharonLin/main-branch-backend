from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated
from datetime import datetime

class PostBase(BaseModel):
    title: Annotated[str, Field(max_length = 50)]
    content: str

class PostCreate(PostBase):
    poster: PositiveInt

class PostRead(PostBase):
    poster: PositiveInt
    id: PositiveInt
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class PostUpdate(PostBase):
    pass