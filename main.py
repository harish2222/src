from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
from src.router import blogs, blogs_post, users, article
from db import models
from db.database import engine


app = FastAPI()
app.include_router(blogs.router)
app.include_router(blogs_post.router)
app.include_router(users.router)
app.include_router(article.router)

@app.get('/')
def index():
    return "Hello World"

#  Parameter based query


@app.get("/sampler")
def para_query():
    return "sampelr para query"
# paraquery  done in internal parameter


@app.get("/sampler/{id}")
def para_query1(id: int):
    return {"messages": f"The value is returned as string {id}"}


class Car_type(str, Enum):
    sedan = "sedan"
    SUV = "Sport Utility Vehicle"
    Coupe = "Coupe"
    GT = "Grand Tour"
    Muscle = "muscle"


@app.get("/car/{car_t}")
def car_type(car_t: Car_type):
    return {"Car_type": f" The car_type you have selected is {car_t}"}


models.Base.metadata.create_all(engine)
