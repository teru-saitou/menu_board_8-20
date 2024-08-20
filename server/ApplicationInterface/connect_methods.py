from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append("/Users/saitouterataka/TrainingProjects/reMenuBoard/server/ApplicationService/SmaregiService")
sys.path.append("/Users/saitouterataka/TrainingProjects/reMenuBoard/server/ApplicationService/ApplicationService")

from routers import menu_router
from routers import phrase_router

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu_router.router)
app.include_router(phrase_router.router)

@app.get("/")
def hello():
    """
    Returns a simple greeting message.

    Returns:
        dict: A dictionary containing a greeting message.
    """
    return {"hello": "Test"}


