from sqlalchemy.orm import Session
from app.model.user import User as user_model
import app.schema.post

schema = app.schema.post

def get_user(db: Session, user_id: int):
    return db.query(user_model).filter(user_model.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model).offset(skip).limit(limit).all()

def get_user_by_name(db: Session, user_name: str):
    return db.query(user_model).filter(user_model.name == user_name).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model).filter(user_model.id == user_id).first()

def create_user(db: Session, user: schema.UserCreate):
    db_user = user_model(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user: user_model):
    db.delete(user)
    db.commit()