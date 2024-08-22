from pydantic import BaseModel, PositiveInt, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    id: PositiveInt
    name: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes = True
    )

class UserWithToken(BaseModel):
    user: UserRead
    access_token: str
    token_type: str

    model_config = ConfigDict(
        from_attributes = True
    )