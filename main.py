from unittest import result
from fastapi import FastAPI
from .model import Item
from .deploiement_model import pred_func
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(data:Item):
    resultat = pred_func(data)
    return {
        "message": "success",
        "data":resultat
        }