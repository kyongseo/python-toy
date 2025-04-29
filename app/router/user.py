from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.model.post import Base
from app.database.database import SessionLocal, engine
from app.schema.user import User, UserCreate
from app.crud.user import get_user_by_name, get_users, get_user
from app.crud.user import create_user as crud_create_user
from app.crud.user import delete_user as crud_delete_user

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
    "",
    response_model=User,
    summary="사용자 생성"
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_name(db, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 이름입니다.")
    return crud_create_user(db=db, user=user)

## 유저 읽기
@router.get(
    "/{user_id}",
    response_model=User,
    summary="사용자 조회"

)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    return db_user

## 모든 유저 조회
@router.get(
    "",
    response_model=List[User],
    summary="사용자 전체 조회"
)
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.delete(
    "/{user_id}",
    summary="사용자 삭제"
)
def delete_user(user_id: int, db:Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    crud_delete_user(db, user=db_user)
    return {"success": True, "message": "사용자가 삭제되었습니다."}