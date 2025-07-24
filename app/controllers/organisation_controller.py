# controllers/organisation_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.organisation_schema import OrganisationCreate, OrganisationOut
from app.services.organisation_service import add_organisation
from app.database import get_db

router = APIRouter(prefix="/organisations", tags=["Organisations"])

@router.post("/create")
def create_organisation_endpoint(payload: OrganisationCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle organisation. Retourne un JSON structuré avec success, message et data.
    Gère aussi les cas d'échec de façon structurée.
    """
    try:
        org = add_organisation(db, payload)
        return {
            "success": True,
            "message": "Organisation créée avec succès.",
            "data": org
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
