from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

####################################
# Para el tipo de la colección debo restrigir las posibilidades.
####################################
import enum

class CollectionType(enum.Enum):
    ALBUM = "ALBUM"
    DECK = "DECK"
    BINDER = "BINDER"
####################################

class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    type = Column(Enum(CollectionType), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow) 

    cards = relationship("CollectionCard", back_populates="collection")