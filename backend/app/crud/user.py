

from sqlalchemy.orm import Session

from app.models import user



def get_user_by_email(db: Session, email: str):
    return db.query(user.User).filter(user.User.email == email).first()

def create_user(db: Session, user: user.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

