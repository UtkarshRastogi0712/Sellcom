from typing import Optional, Union
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(..., max_length=20)
    hashed_password: str = Field(..., max_length=16)
    disabled: bool
