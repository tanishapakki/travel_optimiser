
import uuid

import uuid

from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.core.config import settings

from datetime import datetime, timedelta
from jose import JWTError, jwt

from app.core.db import get_db
from app.models.user import User
from app.core.blacklist import is_blacklisted

#Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#JWT secret key and algorithm
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    """
    Hashes a plain password using bcrypt.

    Args:
        password (str): The plain password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta  | None = None) -> str:
    """
    Creates a JWT access token.

    Args:
        data (dict): The data to include in the token payload.
        expires_delta (timedelta | None): Optional expiration time.

    Returns:
        str: The generated JWT access token.
    """
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "jti": str(uuid.uuid4())})  # Include user_id in the token payload
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # type: ignore
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    Decodes a JWT access token.

    Args:
        token (str): The JWT access token to decode.

    Returns:
        dict: The decoded token payload.
    """
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore
        return decoded_jwt
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/v1/login")



def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the provided JWT token.

    Args:
        db (Session): The database session.
        token (str): The JWT access token.

    Returns:
        User: The current user object.
    """
    try:
        payload = decode_access_token(token)
        if is_blacklisted(payload.get("jti")):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been blacklisted")
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
        )
    

    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
        )
    
    return user

