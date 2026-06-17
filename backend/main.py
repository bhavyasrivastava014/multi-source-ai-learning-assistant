from fastapi import FastAPI
from routes.upload import router as upload_router

app = FastAPI(title="Multi-Source AI Learning Assistant")

app.include_router(upload_router)


@app.get("/")
def home():
    return {"message": "Backend running successfully!"}