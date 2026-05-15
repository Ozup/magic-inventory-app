import requests
from models import Base, Collection
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db

from pydantic import BaseModel #FastAPI lee, valida y convierte con esto, sirve para el CRUD

app = FastAPI()
class CollectionCreate(BaseModel):
    name: str
Base.metadata.create_all(bind=engine)

@app.get("/search/{card_name}")
def search_card(card_name: str):

    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"

    response = requests.get(url)

    data = response.json()

    return {
        "name": data["name"],
        "image": data["image_uris"]["normal"]
    }

@app.get("/collections")
def get_collections(db: Session = Depends(get_db)):
    collections = db.query(Collection).all()
    return [
    {
        "id": "collection.id",
        "name": collection.name
    }
    for collection in collections
]

@app.post("/collections")
def create_collection(
    collection: CollectionCreate,
    db: Session = Depends(get_db)
):

    new_collection = Collection(
        name=collection.name
    )

    db.add(new_collection)

    db.commit()

    db.refresh(new_collection)

    return {
        "id": new_collection.id,
        "name": new_collection.name
    }