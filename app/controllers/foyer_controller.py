# controllers/foyer_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.foyer_schema import FoyerCreate, FoyerOut
from app.database import get_db
from app.services.foyer_service import ajouter_foyer

router = APIRouter(prefix="/foyers", tags=["Foyers"])

@router.post("/create")
def create_foyer_endpoint(foyer_data: FoyerCreate, db: Session = Depends(get_db)):
    try:
        foyer = ajouter_foyer(db, foyer_data)
        return {
            "success": True,
            "message": "Foyer créé avec succès.",
            "data": foyer
        }
    except ValueError as e:
        return {
            "success": False,
            "message": str(e),
            "data": None
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Erreur interne du serveur : " + str(e),
            "data": None
        }
