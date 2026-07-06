from fastapi import FastAPI

app = FastAPI(
    title="Travel Optimizer API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Welcome to the Travel Optimizer API!"}

