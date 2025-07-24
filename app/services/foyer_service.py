# services/foyer_service.py

from sqlalchemy.orm import Session
from app.repository.foyer_repo import create_foyer, get_foyer_by_identite
from app.schemas.foyer_schema import FoyerCreate

def ajouter_foyer(db: Session, foyer_data: FoyerCreate):
    # Vérification de l'existence du foyer
    existing = get_foyer_by_identite(db, foyer_data.nom_foyer, foyer_data.contact)
    if existing:
        raise ValueError("Le foyer existe déjà.")

    return create_foyer(db, foyer_data)
