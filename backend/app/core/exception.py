

from fastapi import Request,FastAPI

from fastapi.responses import JSONResponse
def register_exception_handlers(app: FastAPI):
    """
    Register custom exception handlers for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    @app.exception_handler(Exception)
    async def generic_exception_handler(
            request: Request,
            exc: Exception):

        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "message": str(exc)},
        )
