from contextlib import asynccontextmanager

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from acta import acta_router

PREFIJO_API: str = "/api"
VERSION_API: str = "/v1"
PREFIJO: str = PREFIJO_API + VERSION_API


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("inicio")
    yield
    print("fin")


app = FastAPI(lifespan=lifespan)

origins = ["frontend:5173", "http://frontend:5173", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(PREFIJO)
async def welcome():
    return {"message": "hola mundo todo ok!"}


app.include_router(acta_router.router, prefix=PREFIJO)
app.mount("/static", StaticFiles(directory="static/pdfs"), name="static")
