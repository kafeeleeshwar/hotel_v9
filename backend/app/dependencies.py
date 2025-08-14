from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_current_admin_user(current_user: models.User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return current_user

def get_current_hotel_manager_user(current_user: models.User = Depends(get_current_user)):
    if current_user.role not in [UserRole.HOTEL_MANAGER, UserRole.ADMIN]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return current_user