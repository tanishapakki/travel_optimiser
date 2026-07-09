import time 
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.health import router as health_router
from app.core.exception import register_exception_handlers
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="Travel Optimizer API",
    version="1.0.0"
)

app.include_router(health_router)
register_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request, call_next):

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    logger.info(
        "%s %s %s %.3fs",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response




@app.get("/")
def root():
    return {"message": "Welcome to the Travel Optimizer API!"}

app.include_router(auth_router)

