from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()
from routers import car
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()#iniciando RestApi

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello": "World"}

app.include_router(car.router)