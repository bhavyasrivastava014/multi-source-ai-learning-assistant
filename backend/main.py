from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router
from routes.chat import router as chat_router
from routes.webpage import router as webpage_router
from routes.youtube import router as youtube_router
from routes.course_chat import router as course_router

app = FastAPI(title="Multi-Source AI Learning Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(webpage_router)
app.include_router(youtube_router)
app.include_router(course_router)

@app.get("/")
def home():
    return {
        "message": "Backend running successfully!"
    }