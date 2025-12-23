import json, os
from typing import List, Dict, Any
from pathlib import Path
from enum import Enum

class Cler(str, Enum):
    users = "users"
    recommendations = "recommendations"
    food_database = "food_database"

path = Path()

chemin_file = path.cwd()/"app"/"data"/"database.json"

def read_db() -> Dict[str, Any]:
    try:
        with open(chemin_file, "r") as file:
            print("chemin:",chemin_file,"\n\n\n")
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "recommendations": [], "food_database": []}

def write_db(data: Dict[str, Any], cler:Cler):
    db = read_db()
    db[cler].append(data)
    print("data:", db)
    #with open(chemin_file, "w") as file:
        #json.dump(db, file, indent=4)

def update_write_db(data: Dict[str, Any]):
    with open(chemin_file, "w") as file:
        json.dump(data, file, indent=4)

def get_user_by_email(email: str) -> Dict[str, Any]:
    data = read_db()
    print("data:", data)
    for user in data.get("users", []):
        if user.get("email") == email:
            return user
    return {}

def get_user_by_id(user_id: str) -> Any:
    data = read_db()
    #data.get("users", [])
    for i in range(len(data.get("users", []))):
        if data.get("user", [])[i]["user_id"] == user_id:
            return i
    return None

