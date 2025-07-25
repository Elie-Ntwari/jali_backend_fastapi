from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.suivi_schema import SuiviCreate, SuiviResponse
from app.database import get_db
from app.services.suivi_service import traiter_suivi
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/suivis", tags=["Suivis"])

@router.post("/add")
def ajouter_suivi(suivi_data: SuiviCreate, db: Session = Depends(get_db)):
    try:
        suivi = traiter_suivi(db, suivi_data)
        return {
            "success": True,
            "message": "Suivi enregistré avec succès.",
            "data": SuiviResponse.from_orm(suivi)
        }

    except ValueError as ve:
        return JSONResponse(status_code=404, content={
            "success": False,
            "message": str(ve),
            "data": None
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "success": False,
            "message": f"Erreur interne: {str(e)}",
            "data": None
        })
