from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import database

Base = database.Base

class User(Base):
    __tablename__  = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="PK")
    name = Column(String(10), unique=True, nullable=False, comment="이름")

    # 연관관계 설정 one to many
    posts = relationship("Post", back_populates="writer")