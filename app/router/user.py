from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model.post import Base
from app.database.database import SessionLocal, engine
from app.schema.post import User, UserCreate
from app.crud.post import get_user_by_name, get_users
from app.crud.post import create_user as crud_create_user
router = APIRouter(prefix="/users", tags=["user"])

Base.metadata.create_all(bind=engine)

# 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## 유저 생성
@router.post(
    "/",
    response_model=User,
    summary="사용자 생성"
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_name(db, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 있는 이름입니다.")
    return crud_create_user(db=db, user=user)

## 유저 읽기
@router.get(
    "/{user_name}",
    response_model=User,
    summary="사용자 1명 조회"

)
def read_user(user_name: str, db: Session = Depends(get_db)):
    db_user = get_user_by_name(db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="유저를 찾을 수 없습니다.")
    return db_user

## 모든 유저 읽기
@router.get(
    "/",
    response_model=List[User],
    summary="사용자 전체 조회"
)
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.delete(
    "/{user_name}",
    summary="사용자 삭제"
)
def delete_user(user_name: str, db:Session = Depends(get_db)):
    db_user = get_user_by_name(db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    return delete_user(db, user=db_user)



