from fastapi import FastAPI
from .routers import flights

app = FastAPI(
  title="Flight Tracker API",
  description="Welcome to my API for tracking flights with OpenSky Network",
  version="1.0.0"
)

app.include_router(flights.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flight Tracker API :)"}
