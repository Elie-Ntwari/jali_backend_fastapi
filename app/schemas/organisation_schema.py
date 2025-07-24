
# schemas/organisation_schema.py

from pydantic import BaseModel, EmailStr
from datetime import datetime

# Schéma pour la création d'une organisation (requête POST)
class OrganisationCreate(BaseModel):
    nom: str
    adresse: str
    email: EmailStr
    telephone: str

# Schéma de retour (réponse)
class OrganisationOut(BaseModel):
    id: int
    nom: str
    adresse: str
    email: EmailStr
    telephone: str
    date_creation: datetime

    class Config:
       from_attributes = True  # Permet la compatibilité avec SQLAlchemy
