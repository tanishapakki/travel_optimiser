

from fastapi import APIRouter, status,Depends, HTTPException

from app import models
from app.core.db import get_db
from app.core.security import create_access_token, hash_password
from app.schemas.user import TokenResponse, UserCreate, UserLogin
from app.crud.user import get_user_by_email, create_user
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/auth/v1",
    tags=["Authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = models.User(name=user.name, email=user.email, password=hashed_password)
    created_user = create_user(db, new_user)
    
    return {"user_id": created_user.id, "name": created_user.name, "email": created_user.email, "message": "User registered successfully"} 

@router.post("/login",response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if not existing_user or not existing_user.verify_password(user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    # Here you would typically generate a JWT token or similar for the authenticated user
    token = create_access_token(data={"sub": str(existing_user.id), "email": existing_user.email})
    
    return TokenResponse(access_token=token, token_type="bearer", user_id=existing_user.id, name=existing_user.name, email=existing_user.email)

