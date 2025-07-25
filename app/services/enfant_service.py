from datetime import datetime
from app.repository.enfant_repository import ajouter_enfant, get_enfant_existant
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.enfant_model import Enfant

from app.services.prediction_service import predict_rechute
from app.services.risque_service import evaluer_risque
from app.models.foyer_model import Foyer
from app.models.organisation_model import Organisation

def create_enfant_avec_prediction(db: Session, data):
    # Vérifier si le foyer existe
    foyer = db.query(Foyer).filter_by(id=data.foyer_id).first()
    if not foyer:
        raise HTTPException(status_code=400, detail="Foyer non trouvé avec l'ID fourni.")

    # Vérifier si l'organisation existe
    organisation = db.query(Organisation).filter_by(id=data.organisation_id).first()
    if not organisation:
        raise HTTPException(status_code=400, detail="Organisation non trouvée avec l'ID fourni.")

    # Vérifier doublon
    enfant_existant = get_enfant_existant(
        db,
        nom=data.nom,
        postnom=data.postnom,
        prenom=data.prenom,
        age_enfant=data.age_enfant,
        foyer_id=data.foyer_id
    )
    if enfant_existant:
        raise HTTPException(status_code=409, detail="L’enfant existe déjà dans ce foyer.")

    # Préparer les features pour le modèle
    features = {
        "Sexe": data.sexe,
        "age_enfant": data.age_enfant,
        "heures_total_travail": data.heures_total_travail,
        "scol_actuelle": data.scol_actuelle,
        "difficulte_fonctionnelle": data.difficulte_fonctionnelle,
        "nb_pieces_cat": data.nb_pieces_cat,
        "quintile_bien_etre_x": data.quintile_bien_etre_x,
        "age_chef": data.age_chef,
        "sexe_chef": data.sexe_chef,
        "niveau_education_mere_recod": data.niveau_education_mere_recod,
        "souffre_punition_physique": data.souffre_punition_physique,
        "travail_enfant_global": data.travail_enfant_global,
        "etat_logement": data.etat_logement,
        "niveau_scol_regroupe": data.niveau_scol_regroupe,
        "favorable_correction_physique": data.favorable_correction_physique,
    }

    score = predict_rechute(features)
    niveau, conseil = evaluer_risque(score)

    nouvel_enfant = Enfant(
        nom=data.nom,
        postnom=data.postnom,
        prenom=data.prenom,
        sobriquet=data.sobriquet,
        sexe=data.sexe,
        age_enfant=data.age_enfant,
        niveau_scol_regroupe=data.niveau_scol_regroupe,
        date_enregistrement=datetime.utcnow(),
        score_initial=score,
        statut_risque=niveau,
        organisation_id=data.organisation_id,
        foyer_id=data.foyer_id
    )

    enfant_ajoute = ajouter_enfant(db, nouvel_enfant)

    return {
        "enfant": enfant_ajoute,
        "score": score,
        "niveau_risque": niveau,
        "conseil": conseil
    }
