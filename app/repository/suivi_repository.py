# app/repositories/suivi_repository.py
from sqlalchemy.orm import Session
from app.models.suivi_model import Suivi

def create_suivi(db: Session, suivi: Suivi) -> Suivi:
    db.add(suivi)
    db.commit()
    db.refresh(suivi)
    return suivi
