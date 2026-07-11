

from datetime import datetime,timedelta

from fastapi import APIRouter, status,Depends, HTTPException

from app import models
from app.core.db import get_db
from app.core.security import create_access_token, decode_access_token, oauth2_scheme, get_current_user, hash_password,verify_password
from app.schemas.user import ForgotPasswordRequest, TokenResponse, UserCreate, UserLogin, UserResponse
from app.crud.user import get_user_by_email, create_user
from sqlalchemy.orm import Session

from app.models.user import User
from app.core.blacklist import blacklist_token

router = APIRouter(
    prefix="/auth/v1",
    tags=["Authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = models.User(name=user.name, email=user.email, password_hash=hashed_password)
    created_user = create_user(db, new_user)
    
    return {"user_id": created_user.user_id, "name": created_user.name, "email": created_user.email, "message": "User registered successfully"} 

@router.post("/login",response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if not existing_user or not verify_password(user.password, existing_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    # Here you would typically generate a JWT token or similar for the authenticated user
    token = create_access_token(data={"sub": str(existing_user.user_id), "email": existing_user.email}, expires_delta=None)
    
    return TokenResponse(access_token=token, token_type="bearer", user_id=existing_user.user_id, name=existing_user.name, email=existing_user.email)

@router.post("/logout")
def logout(payload: dict = Depends(oauth2_scheme)):
    # Invalidate the token on the client side (e.g., remove it from local storage or cookies)
    # Optionally, you can implement server-side token invalidation if needed
    payload = decode_access_token(payload)
    ttl=payload.get("exp") - int(datetime.utcnow().timestamp())
    if ttl > 0:
        blacklist_token(payload["jti"], ttl)
    return {"message": "User logged out successfully"}

@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, request.email)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Here you would typically generate a password reset token and send it via email
    reset_token = create_access_token(data={"sub": str(existing_user.user_id), "email": existing_user.email, "type": "password-reset"}, expires_delta=timedelta(seconds=900))
    print("=" * 50)
    print("PASSWORD RESET TOKEN")
    print(reset_token)
    print("=" * 50)
    
    return {"message": "Password reset instructions sent to your email"}

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

