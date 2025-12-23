from pydantic import BaseModel
import datetime
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    age: int
    weight: float
    height: float
    gender: str
    health_conditions: Optional[List[str]] = []
    allergies: Optional[List[str]] = []
    activity_level: str

class FoodItem(BaseModel):
    name: str
    calories: float
    nutrients: Dict[str, float | int]

class Meal(BaseModel):
    meal_type: str
    foods: List[FoodItem]

class FoodLog(BaseModel):
    date: str
    meals: List[Meal]

class User(BaseModel):
    user_id: str
    email: str
    password: str
    profile: Optional[UserProfile] = None
    food_log: Optional[List[FoodLog]] = []