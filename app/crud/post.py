from sqlalchemy.orm import Session

from app.model.post import Post as post_model
from app.model.user import User as user_model

from app.schema.post import Post, PostCreate, UserCreate


def get_user(db: Session, user_id: int):
    return db.query(user_model).filter(user_model.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model).offset(skip).limit(limit).all()

def get_user_by_name(db: Session, user_name: str):
    return db.query(user_model).filter(user_model.name == user_name).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model).filter(user_model.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = user_model(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user: user_model):
    db.delete(user)
    db.commit()

def get_post(db: Session, post_id: int):
    return db.query(post_model).filter(post_model.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(post_model).offset(skip).limit(limit).all()

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = post_model(**post.model_dump(), writer_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post: Post, updated_post: PostCreate):
    post.title = updated_post.title
    post.content = updated_post.content
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()