from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.enfant_schema import EnfantCreate
from app.services.enfant_service import create_enfant_avec_prediction
from app.database import get_db

router = APIRouter(prefix="/enfants", tags=["Enfants"])

@router.post("/create")
def creer_enfant(payload: EnfantCreate, db: Session = Depends(get_db)):
    try:
        result = create_enfant_avec_prediction(db, payload)
        return {
            "success": True,
            "message": "Enfant enregistré avec prédiction réussie.",
            "data": result
        }
    except HTTPException as http_exc:
        return {
            "success": False,
            "message": f"{http_exc.detail}",
            "data": None
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Erreur inattendue : {str(e)}",
            "data": None
        }
