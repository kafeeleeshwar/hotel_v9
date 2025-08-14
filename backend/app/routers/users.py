from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=schemas.UserResponse)
def get_current_user_profile(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=schemas.UserResponse)
def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if user.password:
        current_user.hashed_password = crud.pwd_context.hash(user.password)
    if user.first_name:
        current_user.first_name = user.first_name
    if user.last_name:
        current_user.last_name = user.last_name
    db.commit()
    db.refresh(current_user)
    return current_user