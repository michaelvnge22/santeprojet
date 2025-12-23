from pydantic import BaseModel
from datetime import date
from typing import List, Dict

class Recommendations(BaseModel):
    user_id: str
    date: str
    daily_menu: Dict[str, List[str]]
    tips: List[str]