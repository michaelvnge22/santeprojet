from fastapi import APIRouter, HTTPException
from app.models.user import User, UserProfile
from app.services.database import read_db, write_db, get_user_by_id

router = APIRouter()

@router.post("/{user_id}/profile")
async def update_profile(user_id: str, profile: UserProfile):
    data = read_db()
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Mettre à jour le profil
    for u in data["users"]:
        if u["user_id"] == user_id:
            u["profile"] = profile.dict()
            break
    
    write_db(data)
    return {"message": "Profile updated successfully"}

@router.get("/{user_id}/profile")
async def get_profile(user_id: str):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.get("profile", {})