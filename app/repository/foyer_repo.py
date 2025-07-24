# repositories/foyer_repository.py

from sqlalchemy.orm import Session
from app.models.foyer_model import Foyer
from app.schemas.foyer_schema import FoyerCreate

def get_foyer_by_identite(db: Session, nom_foyer: str, contact: str):
    return db.query(Foyer).filter(Foyer.nom_foyer == nom_foyer, Foyer.contact == contact).first()

def create_foyer(db: Session, foyer_data: FoyerCreate):
    db_foyer = Foyer(**foyer_data.model_dump())
    db.add(db_foyer)
    db.commit()
    db.refresh(db_foyer)
    return db_foyer
