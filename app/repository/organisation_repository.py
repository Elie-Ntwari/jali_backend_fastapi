
# repositories/organisation_repository.py

from sqlalchemy.orm import Session
from app.models.organisation_model import Organisation
from app.schemas.organisation_schema import OrganisationCreate

# Fonction pour insérer une nouvelle organisation dans la BDD
def create_organisation(db: Session, organisation_data: OrganisationCreate) -> Organisation:
    new_org = Organisation(**organisation_data.model_dump()) 
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org


def get_organisation_by_email(db: Session, email: str):
    return db.query(Organisation).filter(Organisation.email == email).first()

