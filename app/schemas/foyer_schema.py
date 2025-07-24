from pydantic import BaseModel, constr
from datetime import datetime

# Schéma utilisé pour la création d’un foyer (requête POST)
class FoyerCreate(BaseModel):
    type_foyer: str
    nom_foyer: str
    adresse: str
    contact: str
    age_chef: int
    sexe_chef: int  # 1=Homme, 2=Femme
    niveau_education_mere_recod: int
    etat_logement: str
    nb_pieces_cat: int

# Schéma utilisé pour la réponse API (retour du foyer)
class FoyerOut(BaseModel):
    id: int
    type_foyer: str
    nom_foyer: str
    adresse: str
    contact: str
    age_chef: int
    sexe_chef: int
    niveau_education_mere_recod: int
    etat_logement: str
    nb_pieces_cat: int
    date_creation: datetime  # Si ce champ est dans la base

    class Config:
         from_attributes = True  # Compatibilité avec SQLAlchemy
