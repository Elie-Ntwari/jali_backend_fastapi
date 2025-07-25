from sqlalchemy.orm import Session
from app.models.enfant_model import Enfant

def get_enfant_existant(db: Session, nom: str, postnom: str, prenom: str, age_enfant: int, foyer_id: int):
    return db.query(Enfant).filter_by(
        nom=nom,
        postnom=postnom,
        prenom=prenom,
        age_enfant=age_enfant,
        foyer_id=foyer_id
    ).first()

def get_enfant_by_id(db: Session, enfant_id: int):
    return db.query(Enfant).filter(Enfant.id == enfant_id).first()

def ajouter_enfant(db: Session, enfant: Enfant):
    db.add(enfant)
    db.commit()
    db.refresh(enfant)
    return enfant
