from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

# request를 받고, response를 보내기 위해 pydantic 모델 사용 - Java/Spring의 DTO 역할
# 데이터베이스에 실제 값을 맵핑하기 위해 SQLAlchemy 모델 사용 - Java/Spring의 Entity 역할

class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    writer_id: int

    class Config:
        from_attributes = True

class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        from_attributes = True