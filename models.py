from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)

    scryfall_id = Column(String)
    name = Column(String)
    mana_cost = Column(String)
    type_line = Column(String)
    rarity = Column(String)
    image_url = Column(String)

class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

class CollectionCard(Base):
    __tablename__ = "collection_cards"

    id = Column(Integer, primary_key=True, index=True)

    collection_id = Column(Integer, ForeignKey("collections.id"))

    card_id = Column(Integer, ForeignKey("cards.id"))

    owned = Column(Boolean, default=False)

    quantity = Column(Integer, default=0)

    foil = Column(Boolean, default=False)