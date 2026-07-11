

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str   

class UserOut(BaseModel):
    user_id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True)
    
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True)
    

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    

