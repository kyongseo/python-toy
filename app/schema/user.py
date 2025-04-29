from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None

class Post(PostBase):
    id: int
    writer_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        from_attributes = True