from fastapi import FastAPI
from routes.upload import router as upload_router
from routes.chat import router as chat_router
from routes.webpage import router as webpage_router
from routes.youtube import router as youtube_router

app = FastAPI(title="Multi-Source AI Learning Assistant")

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(webpage_router)
app.include_router(youtube_router)

@app.get("/")
def home():
    return {"message": "Backend running successfully!"}