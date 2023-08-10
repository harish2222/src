from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()


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


# creating a get method with parameter method

@app.get("/blog/all")
def parameter_testing(para1: int = 1, para2: Optional[int] = None):
    return {"message": f"the parameter are {para1} {para2}"}
