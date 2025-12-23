from fastapi import APIRouter, HTTPException, Form, status
from fastapi.responses import RedirectResponse
from app.models.user import User
from app.services.database import read_db, write_db, get_user_by_email
import bcrypt
from app.services.database import Cler
import uuid
router = APIRouter()

@router.post("/register")
async def register(full_name: str = Form(...), email: str = Form(...), password: str = Form(...), conf_pass:str = Form(...)):
    
    # Vérifier si l'utilisateur existe déjà
    if get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if password != conf_pass:
        raise HTTPException(detail="mot de pass different", status_code=status.HTTP_400_BAD_REQUEST)

    # Hacher le mot de passe
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_data = {
        "user_id": uuid.uuid4(),
        "full_name": full_name,
        "email": email,
        "password": hashed_password.decode('utf-8'),
        "profile": None,
        "food_log": []
    }
    # Ajouter l'utilisateur
    write_db(user_data, Cler.users)
    return RedirectResponse(url="/login?message=Inscription réussie", status_code=309)

@router.post("/login")
async def login_post(email: str = Form(...), password: str = Form(...)):
    user = get_user_by_email(email)
    print("user:", user)
    if not user:
        raise HTTPException(detail="/login?message=Utilisateur non trouvé", status_code=302)
    
    # Vérifier le mot de passe
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        raise HTTPException(detail="/login?message=Mot de passe incorrect", status_code=302)
    
    return RedirectResponse(url="/dashboard?message=Connecté", status_code=302)
