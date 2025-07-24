from pydantic import BaseModel
from typing import Optional

class EnfantCreate(BaseModel):
    nom: str
    postnom: str
    prenom: str
    sobriquet: Optional[str]
    sexe: int
    age_enfant: int
    niveau_scol_regroupe: int
    organisation_id: int
    foyer_id: int

    # Champs liés au modèle (obligatoires côté client)
    heures_total_travail: float
    scol_actuelle: bool
    difficulte_fonctionnelle: bool
    nb_pieces_cat: int
    quintile_bien_etre_x: float
    age_chef: int
    sexe_chef: int
    niveau_education_mere_recod: float
    souffre_punition_physique: bool
    travail_enfant_global: bool
    etat_logement: str
    favorable_correction_physique: bool
