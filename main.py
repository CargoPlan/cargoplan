import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings
from database_connector import init_models

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def app_root():
    return {
        "status": "ok",
        "message": "pong",
    }


if __name__ == '__main__':
    if settings.INIT_MODELS:
        asyncio.run(init_models())

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
