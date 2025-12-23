from typing import Dict, List
from datetime import date

def generate_recommendation(user: Dict) -> Dict:
    profile = user.get("profile", {})
    health_conditions = profile.get("health_conditions", [])
    
    # Logique simple pour les recommandations
    if "diabetes" in health_conditions:
        return {
            "user_id": user["user_id"],
            "date": str(date.today()),
            "daily_menu": {
                "breakfast": ["Oatmeal with berries"],
                "lunch": ["Grilled chicken, vegetables"],
                "dinner": ["Fish, quinoa"]
            },
            "tips": ["Avoid high-sugar foods", "Eat more fiber"]
        }
    return {
        "user_id": user["user_id"],
        "date": str(date.today()),
        "daily_menu": {
            "breakfast": ["Eggs, whole-grain toast"],
            "lunch": ["Salad with chicken"],
            "dinner": ["Pasta with vegetables"]
        },
        "tips": ["Stay hydrated", "Exercise 30 min daily"]
    }