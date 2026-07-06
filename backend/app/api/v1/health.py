

from sqlalchemy import text

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db

router = APIRouter(tags=["Health Check"])

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """
    Health check function to verify the application's health status.
    Returns a dictionary indicating the health status.
    """
    db.execute(text("SELECT 1"))  # Simple query to check database connectivity
    return {"status": "healthy",
            "database": "connected" if db else "disconnected"}