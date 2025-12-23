from pydantic import BaseModel
from typing import Dict

class Food(BaseModel):
    food_id: str
    name: str
    calories: float
    nutrients: Dict[str, float | int]