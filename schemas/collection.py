from pydantic import BaseModel
from models.enums import CollectionType


class CollectionCreate(BaseModel):
    name: str
    type: CollectionType


class CollectionResponse(BaseModel):
    id: int
    name: str
    type: CollectionType

    class Config:
        from_attributes = True