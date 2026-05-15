from fastapi import FastAPI
import requests
from database import engine
from models import Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/") 
def home():
    return {"message": "Hola Samuel"}

@app.get("/search/{card_name}")
def search_card(card_name: str):

    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"

    response = requests.get(url)

    data = response.json()

    return {
        "name": data["name"],
        "image": data["image_uris"]["normal"]
    }