from fastapi import APIRouter, HTTPException
from app.services.database import read_db, write_db, get_user_by_id
from app.services.nutrition import generate_recommendation
from datetime import date

router = APIRouter()

@router.get("/{user_id}")
async def get_recommendations(user_id: str):
    data = read_db()
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Vérifier si une recommandation existe déjà pour aujourd'hui
    for rec in data["recommendations"]:
        if rec["user_id"] == user_id and rec["date"] == str(date.today()):
            return rec
    
    # Générer une nouvelle recommandation
    recommendation = generate_recommendation(user)
    data["recommendations"].append(recommendation)
    write_db(data)
    return recommendation