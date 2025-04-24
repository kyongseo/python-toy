from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import post as posts
from app.model.post import Base
from app.database.database import SessionLocal, engine
from app.schema.post import Post, PostCreate
from app.crud.post import get_post, get_posts, update_post, get_user_by_name

router = APIRouter(prefix="/posts", tags=["post"])

Base.metadata.create_all(bind=engine)

# 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 게시물 생성
@router.post(
    "/users/{user_name}/posts/",
    response_model=Post,
    summary="글 작성"
)
def create_post(user_name: str, post: PostCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_name(db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="유저를 찾을 수 없습니다.")
    return posts.create_post(db, post=post, user_id=db_user.id)

# 모든 게시물 읽기
@router.get(
    "/",
    response_model=List[Post],
    summary="글 목록"
)
def read_posts(db: Session = Depends(get_db)):
    return get_posts(db)

# 게시물 읽기
@router.get(
    "/{post_id}",
    response_model=Post,
    summary="글 상세"
)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return db_post

# 게시물 수정
@router.put(
    "/{post_id}",
    response_model=Post,
    summary="글 수정"
)
def update_post(post_id: int, updated_post: PostCreate, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return update_post(db, post=db_post, updated_post=updated_post)

# 게시물 삭제
@router.delete(
    "/{post_id}",
    summary="글 삭제"
)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    posts.delete_post(db, post=db_post)
    return {"message": "게시글이 삭제되었습니다."}


