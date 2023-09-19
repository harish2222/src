from fastapi import FastAPI, status, Response, Request, HTTPException
from enum import Enum
from typing import Optional
from src.router import blogs, blogs_post, users, article, product
from db import models
from db.database import engine
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException


app = FastAPI()
app.include_router(blogs.router)
app.include_router(blogs_post.router)
app.include_router(users.router)
app.include_router(article.router)
app.include_router(product.router)


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


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exp: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'detail': exp.name}
    )


# @app.exception_handler(HTTPException)
# def custom_HTTPException(request: Request, exp: StoryException):
#     return PlainTextResponse(str(exp), status_code=status.HTTP_400_BAD_REQUEST)


models.Base.metadata.create_all(engine)
