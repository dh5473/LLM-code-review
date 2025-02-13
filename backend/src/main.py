from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.review import router as review_router

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_router.router)
