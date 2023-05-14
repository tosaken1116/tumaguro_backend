from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.db.database import engine
from api.db.models import Base
from api.routers.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="tumaguro"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
