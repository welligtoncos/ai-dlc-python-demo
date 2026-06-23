from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import init_db
from app.routers import tasks


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(tasks.router)
