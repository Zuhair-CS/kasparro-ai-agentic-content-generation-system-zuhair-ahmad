from pydantic import BaseModel
from typing import List

class ProductSchema(BaseModel):
    name: str
    concentration: str
    skin_type: List[str]
    ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: str
