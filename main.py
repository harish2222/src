from fastapi import FastAPI

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
def para_query1(id : int) -> str:
    return f"The value is returned as string {id}"

