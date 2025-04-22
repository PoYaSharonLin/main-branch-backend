from pydantic import BaseModel, PositiveInt, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    id: PositiveInt
    name: str
    role: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

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

class UserProfile(UserBase):
    pass