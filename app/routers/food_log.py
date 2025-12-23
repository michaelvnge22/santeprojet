from fastapi import APIRouter, HTTPException, Form
from app.models.user import FoodLog
from app.services.database import read_db, write_db, get_user_by_id, Cler, update_write_db

router = APIRouter()

@router.post("/{user_id}/add")
async def add_food_log(user_id: str, food_log: FoodLog = Form(...)):
    data = read_db()
    user = get_user_by_id(user_id)
    if not isinstance(user, int):
        raise HTTPException(status_code=404, detail="User not found")
    
    # Ajouter le journal alimentaire
    food = {
        "data":food_log.date
    }
    data["users"][user]["food_log"].append(food)

    update_write_db(data)

    return {"message": "Food log added successfully"}

@router.get("/{user_id}")
async def get_food_log(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.get("food_log", [])