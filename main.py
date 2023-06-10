from fastapi import FastAPI
from os import environ as env

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": f"Githbu changes - You are in {env['MY_VARIABLE']}"}
