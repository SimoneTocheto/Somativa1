import random

from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello World"}

# 127.0.0.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "numero_aleatorio": random.randint(0, 1000)}
