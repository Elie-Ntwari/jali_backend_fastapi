# services/organisation_service.py

from sqlalchemy.orm import Session
from app.repository.organisation_repository import create_organisation, get_organisation_by_email
from app.schemas.organisation_schema import OrganisationCreate

def add_organisation(db: Session, data: OrganisationCreate):
    existing_org = get_organisation_by_email(db, data.email)
    if existing_org:
        raise ValueError("Une organisation avec cet email existe déjà.")
    return create_organisation(db, data)
