
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class SuiviCreate(BaseModel):
    enfant_id: int
    agent_id: int

    heures_total_travail: int
    scol_actuelle: bool
    quintile_bien_etre_x: float
    difficulte_fonctionnelle: bool
    souffre_punition_physique: bool
    travail_enfant_global: bool
    niveau_scol_regroupe: int
    favorable_correction_physique: bool

    commentaire_agent: Optional[str] = None


class SuiviResponse(BaseModel):
    id: int
    enfant_id: int
    agent_id: int
    date_suivi: datetime
    heures_total_travail: int
    scol_actuelle: bool
    difficulte_fonctionnelle: bool
    souffre_punition_physique: bool
    travail_enfant_global: bool
    niveau_scol_regroupe: int
    quintile_bien_etre_x: float
    favorable_correction_physique: bool
    score_suivi: float
    statut_risque: str
    commentaire_agent: Optional[str]
    conseil_personnalise: Optional[str]

    class Config:
        from_attributes = True
