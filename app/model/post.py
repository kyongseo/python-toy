from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import database
from sqlalchemy.sql import func

Base = database.Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    # 처음 데이터 삽입 시 default로 생성일자 생성
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # 데이터가 수정 될 때 자동으로 수정일자 업데이트
    modified_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    # 자식 테이블이 부모 테이블을 참조
    writer_id = Column(Integer, ForeignKey("users.id"))
    writer = relationship("User", back_populates="posts")

